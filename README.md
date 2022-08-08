# morse_code_exam_cheater
Decodes morse code imput from ESP32 IO, sends to an API, and plays back inear tts or vibration motor that you can hide... anywhere.<br>

<center>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~<br>
<b>Updated to Lolin32!!<br></b>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<br>
</center>

<img src="https://raw.githubusercontent.com/E-Krabs/Morse-Code-Exam-Cheater-Raspbery-Pi/main/lolin32_pcb.png"></img>

Translates morse inputs from IO, decodes them, and searches either <a href="https://api.dictionaryapi.dev">Dictionaryapi.dev</a>, or <a href="https://spanishdict.com">Spanishdict</a> or http://api.mathjs.org.
Also plays line by line in a text file with TTS. TTS has been replaced with vibration motor.

<ul>
  <li>Button --> Morse</li>
  <li>Morse --> Word</li>
  <li>Word --> Dictonary/Algebra/Translator</li>
  <li>Result --> Morse</li>
  <li>Morse --> Vibration Motor</li>
</ul>

<h1>Parts List!</h1>
<ul>
  <li><b>Amazon:</b></li>
  <li>Lolin32 V1</li>
  <li><a href="https://www.amazon.com/dp/B07PHRX7QH?psc=1&ref=ppx_yo2ov_dt_b_product_details">Vibration Motor</a></li>
  <li><a href="https://www.amazon.com/dp/B08YN5CPBN?psc=1&ref=ppx_yo2ov_dt_b_product_details">Transmitter and Reciever</a></li>
  <li><a href="https://www.amazon.com/dp/B09DPNCLQZ?psc=1&ref=ppx_yo2ov_dt_b_product_details">Battery</a></li>
  <li><a href="https://www.amazon.com/dp/B07C2Z2VSG?psc=1&ref=ppx_yo2ov_dt_b_product_details">12v Batt holder for transmitter</a></li>
  <li><b>Digikey:</b></li>
  <li>http://www.digikey.com/short/32bw9j7z</li>
  <li><a href="https://www.digikey.com/en/products/detail/c-k/OS102011MA1QN1/1981430">Slide switch SPDT</a></li>
  <li><a href="https://www.digikey.com/en/products/detail/jst-sales-america-inc/S2B-PH-K-S-LF-SN/926626">JST connector</a></li>
</ul>
How I use??
Upload boot.py and main.py to the ESP32. Tape the vobration motor to your theigh. Place buttons under both big toes.<br>
Im tring different buttons that are quiet but flexible to be comfortable to wear.<br>
<ul>
  <li>LToe: 0 (dot)<br></li>
  <li>RToe: 1 (dash)<br></li>
Wait 2 seconds between morse character, wait 5 seconds to enter search.
</ul><br>

NOTES:<br>
<ol>
  <li><b>This board has audio functionality, but was replaced with the vibrator; I was worried you could see the earpiece. You can enable it in <code>main.py</code></b></li>
  <li><b>DONE:</b> RPi Zero W is overkill. I could use a different microcontoller with micro python with internet.<br></li>
  <li>Its nothing weird on the front i promise, you can remove in <code>.kicad_pcb</code><br></li>
  <li><b>DONE:</b> Replace RPi with Teensy or Pico and download entire API to SD as JSON.</b><br></li>
  <li>Beware of polarity on battery from amazon, it may be switched.</li>
  <li>If you want to build one, use JLCPCB, and upload the three .zips.</li>
  <li>Im very sad cause i already printed the boards with silk screen overlapping, so it looks retarded...</li>
  <li>Raspberry pi was updated to an ESP32, cause the Raspberry pi zero is not in production rn and is expesive.</li>
</ol>
