# morse-code-definitions
Takes encoded words and scrapes their definition and part of speech. Converts to text-to-speech.

Translates morse inputs from GPIO on RPi, decodes them, and searches either <a href="https://api.dictionaryapi.dev">Dictionaryapi.dev</a>, or <a href="https://spanishdict.com">Spanishdict</a>.
Then, neatly displays everything on an OLED and reads it to you with gTTS. I had some issues with <code>oled.clear()</code>, thats why refreshing the screen is so sloppy. Also, no functions were used. It's pretty basic.
Also, this script features a crude menu selector. Lots of work still needs to be done. I should mention, this script was written for a RPi Zero W so i could cheat in a Spanish class. But,
the script can be adapted to fit almost any class!

Upcoming Plans::<br>
Use openCV to read a study guide, extract each individual line, and read them to you.
