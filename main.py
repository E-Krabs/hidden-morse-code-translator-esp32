from bs4 import BeautifulSoup
import urllib.request
from urllib.request import Request, urlopen
import dicttoxml
import json
import gtts
from playsound import playsound

try:
	character = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']
	code = ['01','1000','1010','100','0','0010','110','0000','00','0111','101','0100','11','10','111','0110','1101','010','000','1','001','0001','011','1001','1011','1100','11111','01111','00111','00011','00001','00000','10000','11000','11100','11110']

	button = open('C:/Scripts/Python/morse code/button.txt', 'r', encoding="utf8")
	#print(buttons)

	buttons = button.readlines()
	#print(buttons)

	phrase = ''

	for i in buttons:
		phrase += i

	def split(phrase):
		return[char for char in phrase]

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
		page = urllib.request.urlopen('https://api.dictionaryapi.dev/api/v2/entries/en_US/{}'.format(dec_msg_str))
	
	except:
		print('Word Does Not Exist!')
		playsound('400.mp3')
		exit()

	content = page.read()
	obj = json.loads(content)
	#print(obj)
	xml = dicttoxml.dicttoxml(obj)
	#print(xml)

	i = 0
	soup = BeautifulSoup(xml, 'xml')
	pos = soup.find_all('partOfSpeech', limit=4)
	pos_str = pos[i].get_text(strip=True)
	definition =  soup.find_all('definition', limit=4)
	def_str = definition[i].get_text(strip=True)

	#print(pos_str)
	#print(def_str)
	print(dec_msg_str + ' - ' + pos_str + ': ' + def_str)

	tts = gtts.gTTS(pos_str + ': ' + def_str, lang='en')
	tts.save('{}.mp3'.format(dec_msg_str))
	playsound('{}.mp3'.format(dec_msg_str))
	
except:
	print('Keyboard Interrupt')
	playsound('interrupt.mp3')