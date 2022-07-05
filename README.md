# morse_code_exam_cheater
Decodes morse code imput from RPi 0 w+ GPIO, sends to an API, and plays back inear tts or vibration motor that you can hide... anywhere.<br>
MODEL 69420
<img src="https://raw.githubusercontent.com/E-Krabs/morse_code_exam_cheater/main/~3D_dark_front.png"></img>
<img src="https://raw.githubusercontent.com/E-Krabs/morse_code_exam_cheater/main/~3D_dark_back.png"></img>

Translates morse inputs from GPIO, decodes them, and searches either <a href="https://api.dictionaryapi.dev">Dictionaryapi.dev</a>, or <a href="https://spanishdict.com">Spanishdict</a>.
Also plays line by line in a text file with tts. Tts has been replaced with vibration motor.

<ul>
  <li>Button --> Morse</li>
  <li>Morse --> Word</li>
  <li>Word --> Dictonary/MATH/Translator</li>
  <li>Result --> Morse</li>
  <li>Morse --> Vibration Motor</li>
</ul>

<h1>Parts List!</h1>
<ul>
  <li><b>Amazon:</b></li>
  <li>Raspberry Pi Zero W</li>
  <li><a href="https://www.amazon.com/dp/B07PHRX7QH?psc=1&ref=ppx_yo2ov_dt_b_product_details">Vibration Motor</a></li>
  <li><a href="https://www.amazon.com/dp/B08YN5CPBN?psc=1&ref=ppx_yo2ov_dt_b_product_details">Transmitter and Reciever</a></li>
  <li><a href="https://www.amazon.com/dp/B08YN5CPBN?psc=1&ref=ppx_yo2ov_dt_b_product_details">Transmitter and Reciever</a></li>
  <li><a href="https://www.amazon.com/dp/B09DPNCLQZ?psc=1&ref=ppx_yo2ov_dt_b_product_details">Battery</a></li>
  <li><a href="https://www.amazon.com/dp/B09MYRVJ65?psc=1&ref=ppx_yo2ov_dt_b_product_details">20x2 Pin Header</a></li>
  <li><a href="https://www.amazon.com/dp/B07MFKKWG5?psc=1&ref=ppx_yo2ov_dt_b_product_details">Headphone jacks</a></li>
  <li><a href="https://www.amazon.com/dp/B08R1MJWK3?psc=1&ref=ppx_yo2ov_dt_b_product_details">Charge board</a></li>
  <li><a href="https://www.amazon.com/dp/B07C2Z2VSG?psc=1&ref=ppx_yo2ov_dt_b_product_details">12v Batt holder for transmitter</a></li>
  <li><b>Digikey:</b></li>
  <li>2x 33nf caps</li>
  <li>2x 10uf caps</li>
  <li>2x 220Ohm resistors</li>
  <li>2x 150Ohm resistors</li>
  <li><a href="https://www.aliexpress.com/item/2251832734091476.html?spm=a2g0o.productlist.0.0.11765d4az0uH2i&algo_pvid=263211c2-3214-4162-9301-3bb8ea627da0&algo_exp_id=263211c2-3214-4162-9301-3bb8ea627da0-26&pdp_ext_f=%7B%22sku_id%22%3A%2266042057184%22%7D&pdp_npi=2%40dis%21USD%21%210.22%21%21%21%21%21%40210318b916570550813852749e847a%2166042057184%21sea">Audio Amp</a></li>
  <li><a href="https://www.digikey.com/en/products/detail/cit-relay-and-switch/KG04ET/12503505">4pos dip switch</a></li>
  <li><a href="https://www.digikey.com/en/products/detail/c-k/OS102011MA1QN1/1981430">Slide switch SPDT</a></li>
  <li><a href="https://www.digikey.com/en/products/detail/mill-max-manufacturing-corp/0906-0-15-20-76-14-11-0/1147048">2x Spring contacts (pogo pins)</a></li>
  <li><a href="https://www.digikey.com/en/products/detail/cui-devices/PJ-083BH/9830155">DC Jack</a></li>
</ul>
How I use??
Connect the RPi to internet. Tape the vobration motor to your theigh through a small hole in your pocket. Place buttons under both big toes, and left heels.<br>
Im tring different buttons that are quiet but flexible to be comfortable to wear.<br>
<ul>
  <li>LToe: 0 (dot)<br></li>
  <li>RToe: 1 (dash)<br></li>
  <li>LHeel: Space<br></li>
Wait 5 seconds of no input will enter morse.
</ul><br>

NOTES:<br>
<ol>
<li>GERBER --> 69420.zip</li>
<li>J8 and J6 are not connected, I forgot to.<br></li>
<li>RPi Zero W is overkill. I could use a different microcontoller with circuit python with internet.<br></li>
<li>Its nothing weird on the front i promise, you can remove in <code>.kicad_pcb</code><br></li>
<li><b>Upcoming: Replace RPi with Teensy or Pico and download entire API to SD as JSON. So no internet needed!</b><br></li>
<li>If you want to build one, use JLCPCB, and upload "69420.zip". They're super cheap if you select 10-18 day shipping and have a coupon!<br>
I ended up paying $3.98 for five boards... as compared to OSHPARK's $36 for 3!</li>
