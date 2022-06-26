# morse_code_exam_cheater
Takes encoded words from RPi and scrapes their result, converts to tts or back to morse with a vibration motor that you can hide... anywhere.

<img src="https://raw.githubusercontent.com/E-Krabs/morse_code_exam_cheater/main/3d_dark_front.png"></img>
<img src="https://raw.githubusercontent.com/E-Krabs/morse_code_exam_cheater/main/3D_dark_back.png"></img>

Translates morse inputs from GPIO, decodes them, and searches either <a href="https://api.dictionaryapi.dev">Dictionaryapi.dev</a>, or <a href="https://spanishdict.com">Spanishdict</a>.
Also plays line by line in a text file with tts. Tts has been replaced with vibration motor.

<ul>
  <li>Button --> Morse</li>
  <li>Morse --> Word</li>
  <li>Word --> Dictonary</li>
  <li>Result --> Morse</li>
  <li>Morse --> Vibration Motor</li>
</ul>

How I use??
Connect the RPi to internet. Tape the vobration motor to your theigh through a small hole in your pocket. Place buttons under BOTH big toes, and BOTH heels. <br>
LToe: 0 (dot)<br>
RToe: 1 (dash)<br>
LHeel: Space<br>
RHeel: Enter

GERBER!!!! --> 69420.zip!!!!

Note: RPi Zero W is overkill. I could use a different microcontoller with circuit python with internet.<br>
Its nothing weird on the front i promise<br>

<b>Upcoming: Replace RPi with Teensy or Pico and download entire API to SD as JSON. So no internet needed!</b><br>
If you want to build one, use JLCPCB, and upload "69420.zip". They're super cheap if you select 10-18 day shipping and have a coupon!<br>
I ended up paying $3.98 for five boards... as compared to OSHPARK's $36 for 3!
