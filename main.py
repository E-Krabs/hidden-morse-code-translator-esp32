import requests
import urllib.request
from urllib.request import Request, urlopen
import random
import json
import gtts
from pygame import mixer
import time
from python_translator import Translator
#from mutagen.mp3 import MP3
#import RPi.GPIO as GPIO
import winsound

mixer.init() # pygame audio

one = 26
zero = 19
space = 6
enter = 5
vb = 15

#GPIO.setmode(GPIO.BCM)
#GPIO.setup(one, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#GPIO.setup(zero, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#GPIO.setup(space, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#GPIO.setup(enter, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#GPIO.setup(vb, GPIO.OUT)

translator = Translator()

def input_gpio():
		# create dictionary
		character = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']
		code = ['01','1000','1010','100','0','0010','110','0000','00','0111','101','0100','11','10','111','0110','1101','010','000','1','001','0001','011','1001','1011','1100','11111','01111','00111','00011','00001','00000','10000','11000','11100','11110']
		phrase_lst = []
		phrase_str = ''

		while True:
			usr_input = input('Enter Code:' )
			phrase_lst.append(usr_input)
			break

			#one_high = GPIO.input(one)
			#if one_high == True:
				#print('1')
				#phrase_lst.append('1')
				#time.sleep(.4)

			#zero_high = GPIO.input(zero)
			#if zero_high == True:
				#print('0')
				#phrase_lst.append('0')
				#time.sleep(.4)

			#space_high = GPIO.input(space)
			#if space_high == True:
				#print('*')
				#phrase_lst.append('*')
				#time.sleep(.4)

			#enter_high = GPIO.input(enter)
			#if enter_high == True:
				#print('Enter')
				#break

		phrase = ''.join(phrase_lst)
		#print(phrase)

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
				print("Original message: " + line)

			# loop through each morse code representation
			for j in range (0,len(new_msg)):
				# get the alphanumeric alphabet based on the dict keys and append to dec_msg
				if new_msg[j] in rev_morse_dict.keys():
					dec_msg.append(rev_morse_dict[new_msg[j]])

			# printing out the decoded message
			dec_msg_str = ''.join(dec_msg)
			print ("Decoded Message is: " + ''.join(dec_msg))
			break
		return(dec_msg_str)
		
def math_solver():
	frac_open = '{'
	frac_close = '}'
	dec_msg_str = 'x+6=9+{4/7}+{(19+1)/(17-5)}'
	
	
	math_url = dec_msg_str[dec_msg_str.find(frac_open)+1 : dec_msg_str.find(frac_close)]


	
	print('https://mathsolver.microsoft.com/en/solve-problem/{}'.format(dec_msg_str))
	page = requests.get('https://api.dictionaryapi.dev/api/v2/entries/en_US/{}'.format(dec_msg_str))
	content = page.text
	print(content)

def dictionary(dec_msg_str):
	try:
		print('https://api.dictionaryapi.dev/api/v2/entries/en_US/{}'.format(dec_msg_str))
		page = requests.get('https://api.dictionaryapi.dev/api/v2/entries/en_US/{}'.format(dec_msg_str))
	except:
		print('404')
		#mixer.music.load('404.mp3') # 404 not found
		#mixer.music.play()
		#time.sleep(3)
		#GPIO.cleanup()
		exit()

	content = page.text

	try:
		results = json.loads(content)
		#print(results)
	except:
		print('400')
		#mixer.music.load('400.mp3') # 400 bad request
		#mixer.music.play()
		#time.sleep(3)
		return False

	r_pos = []
	r_def = []
	for obj in results:
		r_word = obj['word']
		for key in obj['meanings']:
			r_pos.append(key['partOfSpeech'])
			for key in key['definitions']:
				r_def.append(key['definition'])

	#r_str = '{}, {}: {}'.format(r_word[0], r_pos[0], r_def[0])
	r_str = r_def[0]
	print(r_str)
	vb_motor_lst((ph_to_morse(r_str)))
	#tts = gtts.gTTS(r_str, lang='en')
	#audio_play(tts_save(dec_msg_str, tts))

def spanish(dec_msg_str):
	result = translator.translate(dec_msg_str, 'english')
	if str(result) == dec_msg_str:
		result = translator.translate(dec_msg_str, 'spanish')

	r_str = '{}: {}'.format(dec_msg_str, result)
	print(r_str)
	r_str = str(result)
	vb_motor_lst((ph_to_morse(r_str)))
	#tts = gtts.gTTS(r_str, lang='en')
	#audio_play(tts_save(dec_msg_str, tts))

def text_doc():
	count = -1
	with open('doc.txt', 'r', encoding='utf-8') as o:
		lines = o.readlines()
		while True:
			#one_high = GPIO.input(one)
			#if one_high == True:
			inl = input('Line: ')
			if inl == '1':
				print('1')
				if count < len(lines):
					count += 1
				#print(lines[count].strip())
				vb_motor_lst((ph_to_morse(lines[count].strip())))
				#tts = gtts.gTTS(lines[count].strip(), lang='en')
				#audio_play(tts_save(lines[count].strip(), tts))
			#zero_high = GPIO.input(zero)
			#if zero_high == True:
			if inl == '0':
				print('0')
				if count > 0:
					count -= 1
				#print(lines[count].strip())
				vb_motor_lst((ph_to_morse(lines[count].strip())))
				#tts = gtts.gTTS(lines[count].strip(), lang='en')
				#audio_play(tts_save(lines[count].strip(), tts))

'''
def tts_save(dec_msg_str, tts):
	rand_id = '{}{}.mp3'.format(dec_msg_str, random.randrange(100000, 1999999))
	tts.save(rand_id)
	return(rand_id)

def audio_play(rand_id):
	mixer.music.load('{}.mp3'.format(rand_id))
	mixer.music.play()
	audio = MP3('{}.mp3'.format(rand_id))
	read_wait = audio.info.length
	print(read_wait)
	time.sleep(read_wait)
'''

def ph_to_morse(phrase):
	phrase = phrase.upper()
	#print(phrase)
	# create dictionary
	character = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9',' ', '+','á','é','í','ó','ú','ü','ñ']
	code = ['01','1000','1010','100','0','0010','110','0000','00','0111','101','0100','11','10','111','0110','1101','010','000','1','001','0001','011','1001','1011','1100','11111','01111','00111','00011','00001','00000','10000','11000','11100','11110','*','+','01','0','00','111','001','001','10']

	# reverse the previous dict as it's easier to access the keys
	zipped_code_char = zip(character, code)
	rev_morse_dict = dict(list(zipped_code_char))
	# initiating a while loop
	while True:
		# empty list to store decoded message
		enc_msg = []
		enc_dic = {}

		new_msg = []#list(phrase)

		for char in phrase:
			if char != ' ' and char != "'":
				new_msg.append(char)
				#if char != phrase[-1]:
				new_msg.append('+')
			elif char == ' ':
				new_msg.append(' ')

		#print(new_msg)
		#print(''.join(new_msg))
		# printing out the original message
		print("Original message: " + phrase)

		for j in range(0, len(new_msg)):
			# get the alphanumeric alphabet based on the dict keys and append to dec_msg
			if new_msg[j] in rev_morse_dict.keys():
				enc_msg.append(rev_morse_dict[new_msg[j]])
				#enc_dic[new_msg[j]] = rev_morse_dict[new_msg[j]]
		#print(enc_dic)

		# printing out the decoded message
		enc_msg = ''.join(enc_msg)
		print("Decoded Message is: " + enc_msg)
		break
	return(enc_msg)

def vb_motor_lst(enc_msg):
	for char in enc_msg:
		if char == '1':
			print('1')
			winsound.Beep(2500, 1000)
			#GPIO.output(vb, GPIO.HIGH)
			#time.sleep(1)
			#GPIO.output(vb, GPIO.LOW)
		elif char == '0':
			print('0')
			winsound.Beep(2500, 500)
			#GPIO.output(vb, GPIO.HIGH)
			#time.sleep(.5)
			#GPIO.output(vb, GPIO.LOW)
		elif char == '+':
			print('+')
			#GPIO.output(vb, GPIO.LOW)
			time.sleep(1)
		elif char == '*':
			print('*')
			#GPIO.output(vb, GPIO.LOW)
			time.sleep(2)

'''
def vb_motor_dic(enc_dic):
	for key in enc_dic:
		for j in enc_dic[key]:
			if j == '0':
				winsound.Beep(2500, 500)
			elif j == '1':
				winsound.Beep(2500, 1000)
			elif j == '+':
				time.sleep(.5)
			elif j == '*':
				time.sleep(.5)
'''

i = 3
if i == 0:
	while True:
		dictionary(input_gpio())
elif i == 1:
	while True:
		spanish(input_gpio())

elif i == 2:
	while True:
		text_doc()

elif i == 3:
	while True:
		math_solver()
