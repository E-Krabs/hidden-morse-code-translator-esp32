from bs4 import BeautifulSoup
import requests
import urllib.request
from urllib.request import Request, urlopen
import dicttoxml
import json
import gtts
from pygame import mixer
from board import SCL, SDA
import busio
from oled_text import OledText
import time
import re
from mutagen.mp3 import MP3
import RPi.GPIO as GPIO


i2c = busio.I2C(SCL, SDA)
oled = OledText(i2c, 128, 64) # create oled
mixer.init() # pygame audio

one = 14
zero = 25
space = 8
enter = 7

GPIO.setmode(GPIO.BCM)
GPIO.setup(one, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(zero, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(space, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(enter, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

i = 0
oled.text('____ADDERALL____', 1)
oled.text('- DICTIONARY', 2)
oled.text('  SPANISH', 3)
oled.text('  READ TXT', 4)
oled.auto_show = False

while True:
	up_high = GPIO.input(one)
	if up_high == True:
		i -= 1
		print('up {}'.format(i))
		time.sleep(.4)

	down_high = GPIO.input(zero)
	if down_high == True:
		i += 1
		print('down {}'.format(i))
		time.sleep(.4)

	enter_high = GPIO.input(enter)
	if enter_high == True:
		oled.text('', 2)
		oled.text('', 3)
		oled.text('', 4)
		break

	if i > 2:
		i = 0

	if i < 0:
		i = 2

	if i == 0:
		oled.text('- DICTIONARY', 2)
		oled.text('  SPANISH', 3)
		oled.text('  READ TXT', 4)
		oled.show()

	if i == 1:
		oled.text('  DICTIONARY', 2)
		oled.text('- SPANISH', 3)
		oled.text('  READ TXT', 4)
		oled.show()

	if i == 2:
		oled.text('  DICTIONARY', 2)
		oled.text('  SPANISH', 3)
		oled.text('- READ TXT', 4)
		oled.show()

oled.clear()
print('i = {}'.format(i))

if i == 0:
	while True:
		# create dictionary
		character = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']
		code = ['01','1000','1010','100','0','0010','110','0000','00','0111','101','0100','11','10','111','0110','1101','010','000','1','001','0001','011','1001','1011','1100','11111','01111','00111','00011','00001','00000','10000','11000','11100','11110']

		print('Enter Word:')
		oled.text('DICTIONARY v1', 1)
		oled.text('', 2)
		oled.show()

		phrase_lst = []
		phrase_str = ''

		while True:
			oled.auto_show = True
			oled.text(phrase_str.join(phrase_lst), 3)
			one_high = GPIO.input(one)
			if one_high == True:
				print('1')
				phrase_lst.append('1')
				time.sleep(.4)

			zero_high = GPIO.input(zero)
			if zero_high == True:
				print('0')
				phrase_lst.append('0')
				time.sleep(.4)

			space_high = GPIO.input(space)
			if space_high == True:
				print('*')
				phrase_lst.append('*')
				time.sleep(.4)

			enter_high = GPIO.input(enter)
			if enter_high == True:
				print('Enter')
				oled.auto_show = False
				break

		phrase = ''.join(phrase_lst)
		#print(phrase)
		#print(phrase_lst)

		# reverse the previous dict as it's easier to access the keys
		zipped_code_char = zip(code,character)
		rev_morse_dict = dict(list(zipped_code_char))
		# initiating a while loop
		while True:
			# empty list to store original message
			ori_msg = []
			# empty list to store decoded message
			dec_msg = []
			# append input_msg (string) to ori_msg (string)
			ori_msg.append(phrase)
			# split each morse code by '*'
			new_msg = phrase.split("*")

			# printing out the original message
			for line in ori_msg: # to print original message without the []
				print("Original message: " + line + "\n")

			# loop through each morse code representation
			for j in range (0,len(new_msg)):
				# get the alphanumeric alphabet based on the dict keys and append to dec_msg
				if new_msg[j] in rev_morse_dict.keys():
					dec_msg.append(rev_morse_dict[new_msg[j]])

			# printing out the decoded message
			dec_msg_str = ''.join(dec_msg)
			print ("Decoded Message is: " + ''.join(dec_msg) + "\n")    # end the infinite while loop
			break

		oled.text('', 1)
		oled.text('', 2)
		oled.text('', 3)
		oled.text('', 4)
		oled.show()

		try:
			print('https://api.dictionaryapi.dev/api/v2/entries/en_US/{}'.format(dec_msg_str))
			page = requests.get('https://api.dictionaryapi.dev/api/v2/entries/en_US/{}'.format(dec_msg_str))

		except:
			oled.clear()
			print('Check Internet Connection!')
			mixer.music.load('404.mp3') # 400 bad request
			mixer.music.play()
			oled.text('404', 1)
			oled.text('Bad Internet Connection!', 2)
			oled.show()
			time.sleep(3)
			oled.clear()
			GPIO.cleanup()
			exit()

		stop = False
		content = page.text
		try:
			obj = json.loads(content)
			#print(obj)

		except:
			oled.clear()
			print('Enter Valid Word!')
			mixer.music.load('400.mp3') # 400 bad request
			mixer.music.play()
			oled.text('400', 1)
			oled.text('Enter Valid Word!', 2)
			oled.show()
			time.sleep(3)
			oled.clear()
			stop = True

		if stop == False:
			xml = dicttoxml.dicttoxml(obj)
			#print(xml)

			i = 0
			soup = BeautifulSoup(xml, features="xml")
			#print(soup)
			pos = soup.find_all('partOfSpeech', limit=4)

			try:
				pos_str = pos[i].get_text(strip=True)

			except:
				oled.clear()
				print('Word Does Not Exist!')
				mixer.music.load('400.mp3') # 400 bad request
				mixer.music.play()
				oled.text(dec_msg_str, 1)
				oled.text('Does Not Exist!', 2)
				oled.show()
				time.sleep(3)
				oled.clear()
				stop = True

			if stop == False:
				definition =  soup.find_all('definition', limit=4)
				def_str = definition[i].get_text(strip=True)

				#print(pos_str)
				#print(def_str)
				dec_msg_pos_str = dec_msg_str + ' - ' + pos_str
				#print(dec_msg_pos_str)
				print(dec_msg_str + ' - ' + pos_str + ': ' + def_str)

				out = re.sub("(.{16})", "\\1\n", def_str, 0, re.DOTALL)
				if len(dec_msg_pos_str) > 20:
					oled.text(dec_msg_str, 1)
					oled.text(pos_str, 2)
					oled.text(out, 3)
					oled.show()
				else:
					oled.text(dec_msg_str + ' - ' + pos_str, 1)
					oled.text(out, 2)
					oled.show()

				tts = gtts.gTTS(dec_msg_str + ' - ' + pos_str + ': ' + def_str, lang='en')
				try:
					tts.save('{}.mp3'.format(dec_msg_str))

				except:
					print('File Already Exists!')

				mixer.music.load('{}.mp3'.format(dec_msg_str))
				mixer.music.play()

				audio = MP3('{}.mp3'.format(dec_msg_str))
				read_wait = audio.info.length
				print(read_wait)
				time.sleep(read_wait)
				oled.text('', 2)
				oled.text('', 3)
				oled.text('', 4)
				oled.show()
				oled.clear()

if i == 1:
	while True:
		# create dictionary
		character = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']
		code = ['01','1000','1010','100','0','0010','110','0000','00','0111','101','0100','11','10','111','0110','1101','010','000','1','001','0001','011','1001','1011','1100','11111','01111','00111','00011','00001','00000','10000','11000','11100','11110']

		print('Enter Word:')
		oled.text('SPANISH v1', 1)
		oled.text('', 2)
		oled.show()

		phrase_lst = []
		phrase_str = ''

		while True:
			oled.auto_show = True
			oled.text(phrase_str.join(phrase_lst), 3)
			one_high = GPIO.input(one)
			if one_high == True:
				print('1')
				phrase_lst.append('1')
				time.sleep(.4)

			zero_high = GPIO.input(zero)
			if zero_high == True:
				print('0')
				phrase_lst.append('0')
				time.sleep(.4)

			space_high = GPIO.input(space)
			if space_high == True:
				print('*')
				phrase_lst.append('*')
				time.sleep(.4)

			enter_high = GPIO.input(enter)
			if enter_high == True:
				print('Enter')
				oled.auto_show = False
				break

		phrase = ''.join(phrase_lst)
		#print(phrase)
		#print(phrase_lst)

		# reverse the previous dict as it's easier to access the keys
		zipped_code_char = zip(code,character)
		rev_morse_dict = dict(list(zipped_code_char))
		# initiating a while loop
		while True:
			# empty list to store original message
			ori_msg = []
			# empty list to store decoded message
			dec_msg = []
			# append input_msg (string) to ori_msg (string)
			ori_msg.append(phrase)
			# split each morse code by '*'
			new_msg = phrase.split("*")

			# printing out the original message
			for line in ori_msg: # to print original message without the []
				print("Original message: " + line + "\n")

			# loop through each morse code representation
			for j in range (0,len(new_msg)):
				# get the alphanumeric alphabet based on the dict keys and append to dec_msg
				if new_msg[j] in rev_morse_dict.keys():
					dec_msg.append(rev_morse_dict[new_msg[j]])

			# printing out the decoded message
			dec_msg_str = ''.join(dec_msg)
			print ("Decoded Message is: " + ''.join(dec_msg) + "\n")    # end the infinite while loop
			break

		oled.text('', 1)
		oled.text('', 2)
		oled.text('', 3)
		oled.text('', 4)
		oled.show()

		content = 'https://www.spanishdict.com/thesaurus/{}'.format(dec_msg_str)
		hdr = {'User-Agent': 'Mozilla/5.0'}
		req = Request(content, headers=hdr)
		read_content = urlopen(req)
		soup = BeautifulSoup(read_content, 'html.parser')
		translation = soup.find('div', {'class' : '_3NkyA05U'}).get_text(strip=True).split('-')
		definition = translation[0]
		word = translation[1]

		#print(dec_msg_str + ' = ' + word)
		#print(word + ' - ' + definition)
		dec_msg_trans_wrd = dec_msg_str + ' - ' + word
		print('{} is {}: {}'.format(dec_msg_str, word, definition))

		out = re.sub("(.{16})", "\\1\n", definition, 0, re.DOTALL)
		if len(dec_msg_trans_wrd) > 20:
			oled.text(dec_msg_str, 1)
			oled.text(word, 2)
			oled.text(definition, 3)
			oled.show()
		else:
			oled.text(dec_msg_str + ' - ' + word, 1)
			oled.text(definition, 2)
			oled.show()

		tts = gtts.gTTS('{} is {}: {}'.format(dec_msg_str, word, definition), lang='en')
		try:
			tts.save('{}.mp3'.format(dec_msg_str))

		except:
			print('File Already Exists!')

		mixer.music.load('{}.mp3'.format(dec_msg_str))
		mixer.music.play()

		audio = MP3('{}.mp3'.format(dec_msg_str))
		read_wait = audio.info.length
		print(read_wait)
		time.sleep(read_wait)
		oled.text('', 2)
		oled.text('', 3)
		oled.text('', 4)
		oled.show()
		oled.clear()
if i == 2:
	print('READ TXT')
