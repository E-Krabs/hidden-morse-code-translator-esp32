from bs4 import BeautifulSoup
import urllib.request
from urllib.request import Request, urlopen
import dicttoxml
import json
import gtts
from playsound import playsound
from googletrans import Translator, constants
from pprint import pprint

try:
	while True:
		character = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']
		code = ['01','1000','1010','100','0','0010','110','0000','00','0111','101','0100','11','10','111','0110','1101','010','000','1','001','0001','011','1001','1011','1100','11111','01111','00111','00011','00001','00000','10000','11000','11100','11110']

		#button = open('C:/Scripts/Python/morse code/button.txt', 'r', encoding="utf8")
		#print(buttons)

		#buttons = button.readlines()
		#print(buttons)

		#phrase = ''

		#for i in buttons:
		#	phrase += i

		#def split(phrase):
		#	return[char for char in phrase]

		#print(phrase)
		print('Enter Word:')
		phrase = input()

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

		try:
			urllib.request.urlopen('https://example.com')

		except:
			print('Check Internet Connection!')
			playsound('404.mp3')
			exit()

		try:
			page = urllib.request.urlopen('https://www.spanishdict.com/translate/{}'.format(dec_msg_str))
		
		except:
			print('Word Does Not Exist!')
			playsound('400.mp3')
			exit()

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
		print('{} is {}: {}'.format(dec_msg_str, word, definition))
		tts = gtts.gTTS('{} is {}: {}'.format(dec_msg_str, word, definition), lang='en')
		try:
			tts.save('{}.mp3'.format(dec_msg_str))

		except:
			print('File Already Exists!')
		playsound('{}.mp3'.format(dec_msg_str))

except:
	print('Keyboard Interrupt')
	playsound('interrupt.mp3')