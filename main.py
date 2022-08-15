from machine import Pin, PWM
from time import sleep
import re
import urequests
'''
import time
import os
import re
import requests
cwd = os.getcwd()
'''
zero = Pin(~, Pin.IN)
one = Pin(~, Pin.IN)
vib = Pin(~, Pin.OUT)

dip1 = True
dip2 = False
dip3 = False
dip4 = False

def morse_input():
	int_lst = []
	while True:
		'''
		usr_input = input('Enter Code:' )
		int_lst.append(usr_input)
		break
		'''
		if zero.value() == True:
			morse_lst.append('0')
			vib.value(1)
			sleep(.5)
			vib.value(0)
			interrupt = time.time()

		if one.value() == True:
			morse_lst.append('1')
			vib.value(1)
			sleep(1)
			vib.value(0)
			interrupt = time.time()

		if time.time()-interrupt >= 2:
			morse_lst.append(' ')
			for cycle in range(0, 2)
				vib.value(1)
				sleep(.1)
				vib.value(0)
			interrupt = time.time()

		if time.time()-interrupt >= 3:
			for cycle in range(0, 4)
				vib.value(1)
				sleep(.1)
				vib.value(0)
			break
	return int_lst

def morse_decode(int_lst):
	character_dic = {'01': 'a', '1000': 'b', '1010': 'c', '100': 'd', '0': 'e', '0010': 'f', '110': 'g', '0000': 'h', '00': 'i', '0111': 'j', '101': 'k', '0100': 'l', '11': 'm', '10': 'n', '111': 'o', '0110': 'p', '1101': 'q', '010': 'r', '000': 's', '1': 't', '001': 'u', '0001': 'v', '011': 'w', '1001': 'x', '1011': 'y', '1100': 'z', '01111': '1', '00111': '2', '00011': '3', '00001': '4', '00000': '5', '10000': '6', '11000': '7', '11100': '8', '11110': '9', '11111': '0', '110011': ' ', '010101': '.', '001100': '?', '10010': '/', '100001': '-', '10110': '(', '101101': ')'}
	morse_str = ''.join(int_lst)
	morse_lst = morse_str.split(' ')
	word_lst = []
	for code in morse_lst:
		for key in character_dic:
			if code == key:
				word_lst.append(character_dic[key])

	word_str = ''.join(word_lst)
	print(word_str)
	return word_str

def translator(word, source, target):
	request = requests.get(f'https://translate.google.com/m?sl={source}&tl={target}&hl={source}&q={word}')
	response = request.text
	compile_ = re.compile(r'<div class="result-container">(.*?)</div>')
	result = compile_.search(str(response))
	return result.group(1)

def math_decode(expression):
	character_dic = {'0110': '%5E', '1': 'sqrt', '111': '(', '1010': ')', '01': '%2B', '000': '-', '100': '%2F', '0': '%3D', '01111': '1', '00111': '2', '00011': '3', '00001': '4', '00000': '5', '10000': '6', '11000': '7', '11100': '8', '11110': '9', '11111': '0'}
	#pwr, sqrt, (, ), add, subtract, divide, equals
	for item in expression:
		encoded_str = ''.join(item)
	encoded_lst = encoded_str.split(' ')
	decoded_lst = []
	for code in encoded_lst:
		decoded_lst.append(character_dic[code])
	decoded_str = ''.join(decoded_lst)
	request = requests.get(f'http://api.mathjs.org/v4/?expr={decoded_str}')
	result = request.text
	return result

#def vibrator(result)

while True:
	if dip1 == True: #en|es
		word = morse_decode(morse_input())
		result = translator(word, 'en', 'es')
		print(result)

	if dip2 == True: #es|en
		word = morse_decode(morse_input())
		result = translator(word, 'es', 'en')
		print(result)

	if dip3 == True: #en|zh-cn
		word = morse_decode(morse_input())
		result = translator(word, 'en', 'zh-cn')
		print(result)

	if dip4 == True: #calcaulator
		expression = morse_input()
		result = math_decode(expression)
		print(result)
