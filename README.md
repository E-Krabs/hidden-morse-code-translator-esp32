# morse_code_exam_cheater
Takes encoded words from RPi and scrapes their result, converts to tts or back to morse with a vibration motor that you can hide... anywhere.

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
