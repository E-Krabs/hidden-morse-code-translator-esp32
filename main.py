import requests
import urllib.request
from urllib.request import Request, urlopen
import random
import json
import gtts
#from pygame import mixer
import time
from python_translator import Translator
#from mutagen.mp3 import MP3
import RPi.GPIO as GPIO
#import winsound

#mixer.init() # pygame audio
translator = Translator()

#RF
one = 26
zero = 24
space = 22
enter = 18
#DIP
dip1 = 19
dip2 = 21
dip3 = 23
dip4 = 29
#VIBRATOR
vib = 35
duty_cycle = 50

GPIO.setmode(GPIO.BCM)
#RF
GPIO.setup(one, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(zero, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(space, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(enter, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#DIP
GPIO.setup(dip1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(dip2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(dip3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(dip4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#VIBRATOR
GPIO.setup(vib, GPIO.OUT)
pwm = GPIO.PWM(vib, 100)

print('Ready')
def input_gpio():
		# create dictionary
		character = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']
		code = ['01','1000','1010','100','0','0010','110','0000','00','0111','101','0100','11','10','111','0110','1101','010','000','1','001','0001','011','1001','1011','1100','11111','01111','00111','00011','00001','00000','10000','11000','11100','11110']
		phrase_lst = []
		phrase_str = ''

		while True:
			#usr_input = input('Enter Code:' )
			#phrase_lst.append(usr_input)
			#break

			one_high = GPIO.input(one)
			if one_high == True:
				print('1')
				phrase_lst.append('1')
				pwm.start(duty_cycle)
				time.sleep(1)
				pwm.stop()
				interrupt = time.time()

			zero_high = GPIO.input(zero)
			if zero_high == True:
				print('0')
				phrase_lst.append('0')
				pwm.start(duty_cycle)
				time.sleep(.3)
				pwm.stop()
				interrupt = time.time()

			space_high = GPIO.input(space)
			if space_high == True:
				print('*')
				phrase_lst.append('*')
				pwm.start(duty_cycle)
				time.sleep(2)
				pwm.stop()
				interrupt = time.time()

			if time.time()-interrupt >= 10:
				print('Enter')
				pwm.start(duty_cycle)
				time.sleep(3)
				pwm.stop()
				break

		phrase = ''.join(phrase_lst)
		#print(phrase)

		# reverse the previous dict as it's easier to access the keys
		zipped_code_char = zip(code, character)
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

def math_solver(dec_msg_str):
	dec_msg_lst = dec_msg_str.split('*')
	math_enc = ['pwr', 'sq', 'po', 'pc', 'pls', 'min', 'div', 'is']
	math_dec = ['~', 'sqrt', '(', ')', '+', '-', '/', '=']
	zipped_math = zip(math_enc, math_dec)
	rev_math_dict = dict(list(zipped_math))
	math_url_lst = []
	for j in range(0, len(dec_msg_lst)):
		if dec_msg_lst[j] in rev_math_dict.keys():
			math_url_lst.append(rev_math_dict[dec_msg_lst[j]])
		else:
			math_url_lst.append(dec_msg_lst[j])
	math_url = ''.join(math_url_lst)
	#print(math_url)
	
	print('https://www.tiger-algebra.com/nojsdrill/{}'.format(math_url))

	try:
		page = requests.get('https://www.tiger-algebra.com/nojsdrill/{}'.format(math_url))
		content = page.text
		soup = BeautifulSoup(content, 'html.parser')
		select = soup.select('div.result:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > span:nth-child(1)')
	except:
		error()
		return None

	for result in select:
		print(result.get_text())
		math_encoder(result.get_text())

def math_encoder(*result):
	math_enc = ['`0110`011`010`', '`000`1101`', '`0110`111`', '`0110`1010`', '`0110`0100`000`', '`11`00`10`', '`100`00`0001`', '`00`000`','11111','01111','00111','00011','00001','00000','10000','11000','11100','11110','1001','1011','1100','0010','110']
	math_dec = ['^', '√', '(', ')', '+', '-', '/', '=', '0','1','2','3','4','5','6','7','8','9','x','y','z','f','g']
	zipped_math = zip(math_dec, math_enc)
	rev_math_dict = dict(list(zipped_math))
	math_enc_lst = []
	math_enc = []
	print('hi')
	for solution in result:
		for char in list(solution):
			math_enc_lst.append(char)
			math_enc_lst.append('`')

		for j in range(0, len(math_enc_lst)):
			if math_enc_lst[j] in rev_math_dict.keys():
				math_enc.append(rev_math_dict[math_enc_lst[j]])
			else:
				math_enc.append(math_enc_lst[j])
		math_enc_str = ''.join(math_enc)
		vib_motor(math_enc_str)

def dictionary(dec_msg_str):
	try:
		print('https://api.dictionaryapi.dev/api/v2/entries/en_US/{}'.format(dec_msg_str))
		page = requests.get('https://api.dictionaryapi.dev/api/v2/entries/en_US/{}'.format(dec_msg_str))
	except:
		print('404')
		error()
		return None

	content = page.text

	try:
		results = json.loads(content)
		#print(results)
	except:
		print('400')
		error()
		return None

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
	morse_encoder(r_str)
	#tts = gtts.gTTS(r_str, lang='en')
	#audio_play(tts_save(dec_msg_str, tts))

def spanish(dec_msg_str):
	result = translator.translate(dec_msg_str, 'english')
	if str(result) == dec_msg_str:
		result = translator.translate(dec_msg_str, 'spanish')

	r_str = '{}: {}'.format(dec_msg_str, result)
	print(r_str)
	r_str = str(result)
	morse_encoder(r_str)
	#tts = gtts.gTTS(r_str, lang='en')
	#audio_play(tts_save(dec_msg_str, tts))

def text_doc():
	count = -1
	with open('doc.txt', 'r', encoding='utf-8') as o:
		lines = o.readlines()
		while True:
			one_high = GPIO.input(one)
			if one_high == True:
			if inl == '1':
				print('1')
				if count < len(lines):
					count += 1
				print(lines[count].strip())
				morse_encoder(lines[count].strip())
				#tts = gtts.gTTS(lines[count].strip(), lang='en')
				#audio_play(tts_save(lines[count].strip(), tts))

			zero_high = GPIO.input(zero)
			if zero_high == True:
				print('0')
				if count > 0:
					count -= 1
				print(lines[count].strip())
				morse_encoder(lines[count].strip())
				#tts = gtts.gTTS(lines[count].strip(), lang='en')
				#audio_play(tts_save(lines[count].strip(), tts))

def tts_save(dec_msg_str, tts):
	rand_id = '{}{}.mp3'.format(dec_msg_str, random.randrange(10000, 199999))
	tts.save(rand_id)
	return(rand_id)

def audio_play(rand_id):
	mixer.music.load(rand_id)
	with mixer.music.play():
		time.sleep(100)

def morse_encoder(phrase):
	phrase = phrase.upper()
	#print(phrase)
	# create dictionary
	character = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9',' ', '-','á','é','í','ó','ú','ü','ñ']
	code = ['01','1000','1010','100','0','0010','110','0000','00','0111','101','0100','11','10','111','0110','1101','010','000','1','001','0001','011','1001','1011','1100','11111','01111','00111','00011','00001','00000','10000','11000','11100','11110','*','-','01','0','00','111','001','001','10']

	# reverse the previous dict as it's easier to access the keys
	zipped_code_char = zip(character, code)
	rev_morse_dict = dict(list(zipped_code_char))
	# initiating a while loop
	while True:
		# empty list to store decoded message
		enc_msg = []

		new_msg = []
		for char in list(phrase):
			new_msg.append(char)
			new_msg.append('`')

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
	vib_motor(enc_msg)

def vib_motor(enc_msg):
	for char in enc_msg:
		if char == '1':
			print('1')
			pwm.start(duty_cycle)
			time.sleep(1)
			pwm.stop()
		elif char == '0':
			print('0')
			pwm.start(duty_cycle)
			time.sleep(.3)
			pwm.stop()
		elif char == '`':
			print('`')
			time.sleep(1)
		elif char == '*':
			print('*')
			time.sleep(3)

def error():
	err_msg = ['0','0','0','*','1','1','1','*','0','0','0']
	for char in err_msg:
		if char == '1':
			pwm.start(duty_cycle)
			time.sleep(1)
			pwm.stop()
		elif char == '0':
			pwm.start(duty_cycle)
			time.sleep(.3)
			pwm.stop()
		elif char == '*':
			time.sleep(1)

dip1_high = GPIO.input(dip1)
if dip1_high == True:
	while True:
		dictionary(input_gpio())

dip2_high = GPIO.input(dip2)
elif dip2_high == True:
	while True:
		spanish(input_gpio())

dip3_high = GPIO.input(dip3)
elif dip3_high == True:
	while True:
		text_doc()

dip4_high = GPIO.input(dip4)
elif dip4_high == True:
	while True:
		math_solver(input_gpio())
