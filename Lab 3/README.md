# Chatterboxes
**NAMES OF COLLABORATORS HERE**

Collaborated with: Tsung-Yin Hsieh (th542@cornell.edu)
The video was filmed by Jonathan Tan(jmt362@cornell.edu)

First, we brainstorm the main idea and the script together. Second, we acted out the dialogue and asked Jonathan to help us film the video. After finishing the main, Tsung-Yin contributed the code of text to speech and speech; Yi-Ru was responsible for drawing the storyboards. 

[![Watch the video](https://user-images.githubusercontent.com/1128669/135009222-111fe522-e6ba-46ad-b6dc-d1633d21129c.png)](https://www.youtube.com/embed/Q8FWzLMobx0?start=19)

In this lab, we want you to design interaction with a speech-enabled device--something that listens and talks to you. This device can do anything *but* control lights (since we already did that in Lab 1).  First, we want you first to storyboard what you imagine the conversational interaction to be like. Then, you will use wizarding techniques to elicit examples of what people might say, ask, or respond.  We then want you to use the examples collected from at least two other people to inform the redesign of the device.

We will focus on **audio** as the main modality for interaction to start; these general techniques can be extended to **video**, **haptics** or other interactive mechanisms in the second part of the Lab.

## Prep for Part 1: Get the Latest Content and Pick up Additional Parts 

### Pick up Web Camera If You Don't Have One

Students who have not already received a web camera will receive their [IMISES web cameras](https://www.amazon.com/Microphone-Speaker-Balance-Conference-Streaming/dp/B0B7B7SYSY/ref=sr_1_3?keywords=webcam%2Bwith%2Bmicrophone%2Band%2Bspeaker&qid=1663090960&s=electronics&sprefix=webcam%2Bwith%2Bmicrophone%2Band%2Bsp%2Celectronics%2C123&sr=1-3&th=1) on Thursday at the beginning of lab. If you cannot make it to class on Thursday, please contact the TAs to ensure you get your web camera. 

### Get the Latest Content

As always, pull updates from the class Interactive-Lab-Hub to both your Pi and your own GitHub repo. There are 2 ways you can do so:

**\[recommended\]**Option 1: On the Pi, `cd` to your `Interactive-Lab-Hub`, pull the updates from upstream (class lab-hub) and push the updates back to your own GitHub repo. You will need the *personal access token* for this.

```
pi@ixe00:~$ cd Interactive-Lab-Hub
pi@ixe00:~/Interactive-Lab-Hub $ git pull upstream Fall2022
pi@ixe00:~/Interactive-Lab-Hub $ git add .
pi@ixe00:~/Interactive-Lab-Hub $ git commit -m "get lab3 updates"
pi@ixe00:~/Interactive-Lab-Hub $ git push
```

Option 2: On your your own GitHub repo, [create pull request](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2022Fall/readings/Submitting%20Labs.md) to get updates from the class Interactive-Lab-Hub. After you have latest updates online, go on your Pi, `cd` to your `Interactive-Lab-Hub` and use `git pull` to get updates from your own GitHub repo.

## Part 1.

### Text to Speech 

In this part of lab, we are going to start peeking into the world of audio on your Pi! 

We will be using the microphone and speaker on your webcamera. In the home directory of your Pi, there is a folder called `text2speech` containing several shell scripts. `cd` to the folder and list out all the files by `ls`:

```
pi@ixe00:~/text2speech $ ls
Download        festival_demo.sh  GoogleTTS_demo.sh  pico2text_demo.sh
espeak_demo.sh  flite_demo.sh     lookdave.wav
```

You can run these shell files by typing `./filename`, for example, typing `./espeak_demo.sh` and see what happens. Take some time to look at each script and see how it works. You can see a script by typing `cat filename`. For instance:

```
pi@ixe00:~/text2speech $ cat festival_demo.sh 
#from: https://elinux.org/RPi_Text_to_Speech_(Speech_Synthesis)#Festival_Text_to_Speech

echo "Just what do you think you're doing, Dave?" | festival --tts
```

Now, you might wonder what exactly is a `.sh` file? Typically, a `.sh` file is a shell script which you can execute in a terminal. The example files we offer here are for you to figure out the ways to play with audio on your Pi!

You can also play audio files directly with `aplay filename`. Try typing `aplay lookdave.wav`.

\*\***Write your own shell file to use your favorite of these TTS engines to have your Pi greet you by name.**\*\*
(This shell file should be saved to your own repo for this lab.)
My shell file link: https://github.com/Peggypei98/Interactive-Lab-Hub/blob/f035eb08d0bbe0a34e9efa3543166e4755f5a4d8/Lab%203/festival_demo.sh



Bonus: If this topic is very exciting to you, you can try out this new TTS system we recently learned about: https://github.com/rhasspy/larynx

### Speech to Text

Now examine the `speech2text` folder. We are using a speech recognition engine, [Vosk](https://alphacephei.com/vosk/), which is made by researchers at Carnegie Mellon University. Vosk is amazing because it is an offline speech recognition engine; that is, all the processing for the speech recognition is happening onboard the Raspberry Pi. 

In particular, look at `test_words.py` and make sure you understand how the vocab is defined. 
Now, we need to find out where your webcam's audio device is connected to the Pi. Use `arecord -l` to get the card and device number:
```
pi@ixe00:~/speech2text $ arecord -l
**** List of CAPTURE Hardware Devices ****
card 1: Device [Usb Audio Device], device 0: USB Audio [USB Audio]
  Subdevices: 1/1
  Subdevice #0: subdevice #0
```
The example above shows a scenario where the audio device is at card 1, device 0. Now, use `nano vosk_demo_mic.sh` and change the `hw` parameter. In the case as shown above, change it to `hw:1,0`, which stands for card 1, device 0.  

Now, look at which camera you have. Do you have the cylinder camera (likely the case if you received it when we first handed out kits), change the `-r 16000` parameter to `-r 44100`. If you have the IMISES camera, check if your rate parameter says `-r 16000`. Save the file using Write Out and press enter.

Then try `./vosk_demo_mic.sh`

\*\***Write your own shell file that verbally asks for a numerical based input (such as a phone number, zipcode, number of pets, etc) and records the answer the respondent provides.**\*\*
https://github.com/Peggypei98/Interactive-Lab-Hub/blob/ca2a29a4a2bc9fc4bd71a76e4341e9ff4c3bfa73/Lab%203/vosk.sh


### Serving Pages

In Lab 1, we served a webpage with flask. In this lab, you may find it useful to serve a webpage for the controller on a remote device. Here is a simple example of a webserver.

```
pi@ixe00:~/Interactive-Lab-Hub/Lab 3 $ python server.py
 * Serving Flask app "server" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 162-573-883
```
From a remote browser on the same network, check to make sure your webserver is working by going to `http://<YourPiIPAddress>:5000`. You should be able to see "Hello World" on the webpage.

### Storyboard

Storyboard and/or use a Verplank diagram to design a speech-enabled device. (Stuck? Make a device that talks for dogs. If that is too stupid, find an application that is better than that.) 

\*\***Post your storyboard and diagram here.**\*\*
![This is an image](https://github.com/Peggypei98/Interactive-Lab-Hub/blob/4a3b9f9f489c6c7c09b85367b0f30b872d459c44/Lab%203/picture1.jpg)
![This is an image](https://github.com/Peggypei98/Interactive-Lab-Hub/blob/4a3b9f9f489c6c7c09b85367b0f30b872d459c44/Lab%203/picture2.jpg)
![This is an image](https://github.com/Peggypei98/Interactive-Lab-Hub/blob/4a3b9f9f489c6c7c09b85367b0f30b872d459c44/Lab%203/picture3.jpg)

Write out what you imagine the dialogue to be. Use cards, post-its, or whatever method helps you develop alternatives or group responses. 

\*\***Please describe and document your process.**\*\*
We want to design a Roosevelt Island tourist guide, Rosy, for tourists to know more about this beautiful place. 

User: Wow, Roosevelt Island seems like an excellent place to visit. I want to ask Rosy to tell me more about this place. Hey, Rosy, how to get to Roosevelt Island?

Rosy: You can get there by Ferry, Subway, Tramway, or Self-drive. Which one do you prefer?

User: I prefer to get there by Tramway.

Rosy: Tramway is a good choice. Remember to bring a Metro card with you. Let me tell you some good places to visit on this island. What do you want to do?

User: I would like to walk around and grab some food. 

Rosy: Frankin D. Roosevelt Four Freedoms Park is on the southern tip of the island, its name inspired by his famous 1941 speech. The park was also the last work of Louis I. Kahn, a renowned 20th-century architect...Oh, it seems like this option is not that appealing to you. How about the Blackwell Island Lighthouse?

User: Wow, It sounds great!! Show me more!!

Rosy: The Blackwell Island Lighthouse is on the other end of the island; at the most northern stretch is a 50-foot-tall lighthouse built by prisoners in 1872. It's now on the National Register of Historic Places and is surrounded by a park with fantastic panoramic views. And you can visit the Cornell Tech campus as well. 

User: Great! How about some good place to eat?

Rosy: Granny Annies's is an Irish bar and kitchen, and Bread and Butter is a good brunch place. 

User: Great!! Thanks for your suggestion!

Rosy: My pleasure. Please rate this service from one to ten. 

User: Eight.

Rosy: Thanks for your rating! Hope you have a wonderful trip! 

### Acting out the dialogue

Find a partner, and *without sharing the script with your partner* try out the dialogue you've designed, where you (as the device designer) act as the device you are designing.  Please record this interaction (for example, using Zoom's record feature).
https://youtu.be/EX9ffuLqr34


\*\***Describe if the dialogue seemed different than what you imagined when it was acted out, and how.**\*\*

While acting out the dialogue, we found that we could add more features in part2. For instance, reporting weather,  planning the best route for users, or even inputting some funny stories related to Roosevelt Island. 


### Wizarding with the Pi (optional)
In the [demo directory](./demo), you will find an example Wizard of Oz project. In that project, you can see how audio and sensor data is streamed from the Pi to a wizard controller that runs in the browser.  You may use this demo code as a template. By running the `app.py` script, you can see how audio and sensor data (Adafruit MPU-6050 6-DoF Accel and Gyro Sensor) is streamed from the Pi to a wizard controller that runs in the browser `http://<YouPiIPAddress>:5000`. You can control what the system says from the controller as well!

\*\***Describe if the dialogue seemed different than what you imagined, or when acted out, when it was wizarded, and how.**\*\*

# Lab 3 Part 2

For Part 2, you will redesign the interaction with the speech-enabled device using the data collected, as well as feedback from part 1.

## Prep for Part 2

1. What are concrete things that could use improvement in the design of your device? For example: wording, timing, anticipation of misunderstandings...
2. What are other modes of interaction _beyond speech_ that you might also use to clarify how to interact?
3. Make a new storyboard, diagram and/or script based on these reflections.

## Prototype your system

The system should:
* use the Raspberry Pi 
* use one or more sensors
* require participants to speak to it. 

*Document how the system works*

Collaborated with: Tsung-Yin Hsieh (th542@cornell.edu)

In the part 2, we also brainstorm the additional features for our system and the script together. After finishing the brainstorming, Tsung-Yin contributed the code of text to speech and the face detection using webcam; Yi-Ru was responsible for drawing the new storyboards. And then, we asked two participants to interact with our system. Finally, we discussed what we learned from the two tests and how can we improve this system.

Additional Dialogue: Our system provides weather information for the tourists who want to go to Roosevelt Island

User: Hey, Rosy! Is today a good time to go to Roosevelt Island?

Rosy: The weather is 75 degrees and it is a sunny day. It’s a great time to visit?

User: How to get to the Roosevelt Island?

Rosy: You can get there by Ferry, Subway, Tramway, or Self-drive. Which one do you prefer?

User: I prefer to get there by Ferry.

Rosy: Ferry is a good choice. The view on the ferry is really good. Let me tell you some good places to visit on this island. What do you want to do?

User: I would like to walk around and grab some food.

Rosy: Cornell Tech is a great place with Tata Innovation Center and Bloomberg Center. It owns diverse environment of academics and practitioners who excel at imagining, researching and building digitally-enabled products and services to directly address societal and commercial needs.

User: Wow, It sounds great!! I would like to study there in the future!!

User: How about some good place to eat?

Rosy: You can grab some food and drinks at the cafe.

User: Great! Thanks for the suggestion!

Rosy: My pleasure. Please rate this service from one to ten.

User: Nine.

Rosy: Thanks for your rating! Hope you have a wonderful trip!

Our redesign stiryboards

![This is an image](https://github.com/Peggypei98/Interactive-Lab-Hub/blob/4ee55c84d7fc081d149eb20a9c4ad4d94f6ee030/Lab%203/picture4.jpg)

![This is an image](https://github.com/Peggypei98/Interactive-Lab-Hub/blob/4ee55c84d7fc081d149eb20a9c4ad4d94f6ee030/Lab%203/picture5.jpg)

![This is an image](https://github.com/Peggypei98/Interactive-Lab-Hub/blob/4ee55c84d7fc081d149eb20a9c4ad4d94f6ee030/Lab%203/picture6.jpg)

*Include videos or screencaptures of both the system and the controller.*

Face Detection with OpenCV through the webcam

![This is an image](https://github.com/Peggypei98/Interactive-Lab-Hub/blob/4ee55c84d7fc081d149eb20a9c4ad4d94f6ee030/Lab%203/picture7.jpg)

## Test the system
Try to get at least two people to interact with your system. (Ideally, you would inform them that there is a wizard _after_ the interaction, but we recognize that can be hard.)

[![Our first test video]](https://youtu.be/Rdltl_4AmTs)

[![Our second test video]](https://youtu.be/8ghjDCK-Rms)


![Link to our code](https://github.com/Peggypei98/Interactive-Lab-Hub/blob/e2a692dbb08cc2715c063d2f0f56de77298c65f3/Lab%203/test_words.py)

![Link to our shell code](https://github.com/Peggypei98/Interactive-Lab-Hub/blob/e2a692dbb08cc2715c063d2f0f56de77298c65f3/Lab%203/tts_lab3_1.sh)

![Link to our shell code](https://github.com/Peggypei98/Interactive-Lab-Hub/blob/e2a692dbb08cc2715c063d2f0f56de77298c65f3/Lab%203/tts_lab3_2.sh)


Answer the following:

Our participants:

Jonathan Tan (jmt362@cornell.edu)

Sylvia Ding (sd569@cornell.edu)



### What worked well about the system and what didn't?
The interaction between our Rosy and users worked well. The weather reporting feature and emotion detection feature made our users feel good while using this service.

Yet, our system did not provide features that can arrange the whole visiting plan for users. Also, our Rosy did not offer an optional choice for users while they were asking about some places to go.

### What worked well about the controller and what didn't?
We had a hard time when switching between the emotion detection interface and VS code, and this made us really hard to combine them together. The rest of our design works pretty well.


### What lessons can you take away from the WoZ interactions for designing a more autonomous version of the system?
The first lesson we can take away from the WoZ interaction for designing a more autonomous version of the system is that try our best to improve the experience by making the process more interesting and engaging. For instance, adding more funny stories into our tourist guide scripts. By doing so, we can make the whole experience more fun.

The second lesson we learn is that different users have different needs, some people prefer visiting a memorial park, and some people might like to walk around the campus. Thus, if we could add some content script for Rosy to read it out for users after they selecting it would be more user-friendly.

### How could you use your system to create a dataset of interaction? What other sensing modalities would make sense to capture?

We could use this system to track all the Roosevelt Island tourists’ choices and emotions. In this way, we can analyze whether some attraction is more popular or more suitable for different people.

The other sensing modalities we may capture are the body language and heart rate of a user. These two sensing modalities can help us determine the user's emotions better.



