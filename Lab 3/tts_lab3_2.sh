#https://elinux.org/RPi_Text_to_Speech_(Speech_Synthesis)

#!/bin/bash
say() { local IFS=+;/usr/bin/mplayer -ao alsa -really-quiet -noconsolecontrols "http://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&q=$*&tl=en"; }
#say $*
say "The temperature today is 75 degrees and it is a sunny day. It's great time to visit Roosevelt Island."
sleep 4s
say "You can get there by Ferry, Subway, Tramway, or Self-drive. Which one do you prefer?"
sleep 4s
say "Ferry is a good choice. The view on the ferry is really good. Let me tell you some good places to visit on this island. What do you want to do?"
sleep 4s
say "Cornell Tech is a great place with Tata Innovation Center and Bloomberg Center."
say "It owns diverse environment of academics and practitioners who excel at imagining, researching and building digitally-enabled products and services to directly address societal and commercial needs."
sleep 8s
say "You can eat at the cafe at Cornell Tech."
sleep 4s
say "My pleasure. Please rate this service from one to ten."
sleep 2s
say "Thanks for your rating! Hope you have a wonderful trip!"
 
