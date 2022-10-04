#https://elinux.org/RPi_Text_to_Speech_(Speech_Synthesis)

#!/bin/bash
say() { local IFS=+;/usr/bin/mplayer -ao alsa -really-quiet -noconsolecontrols "http://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&q=$*&tl=en"; }
#say $*
say "You can get there by Ferry, Subway, Tramway, or Self-drive. Which one do you prefer?"
sleep 5s
say "Tramway is a good choice. Remember to bring a Metro card with you. Let me tell you some good places to visit on this island. What do you want to do?"
sleep 5s
say "Franklin D. Roosevelt Four Freedoms Park is on the southern tip of the island, its name inspired by his famous 1941 speech." 
say "The park was also the last work of Louis I. Kahn, a renowned 20th-century architect...Oh, it seems like this option is not that appealing to you. How about the Blackwell Island Lighthouse?"
sleep 5s
say "The Blackwell Island Lighthouse is on the other end of the island; at the most northern stretch is a 50-foot-tall lighthouse built by prisoners in 1872." 
say "It's now on the National Register of Historic Places and is surrounded by a park with fantastic panoramic views."
sleep 5s
say "Granny Annies's is an Irish bar and kitchen, and Bread and Butter is a good brunch place."
sleep 3s
say "My pleasure. Please rate this service from one to ten."
sleep 2s
say "Thanks for your rating! Hope you have a wonderful trip!"
 
