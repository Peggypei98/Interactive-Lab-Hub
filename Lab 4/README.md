# Ph-UI!!!

**NAMES OF COLLABORATORS HERE**

Collaboratad with 

Tsung-Yin Hsieh th542


For lab this week, we focus both on sensing, to bring in new modes of input into your devices, as well as prototyping the physical look and feel of the device. You will think about the physical form the device needs to perform the sensing as well as present the display or feedback about what was sensed. 

## Part 1 Lab Preparation

### Get the latest content:
As always, pull updates from the class Interactive-Lab-Hub to both your Pi and your own GitHub repo. As we discussed in the class, there are 2 ways you can do so:

**\[recommended\]**Option 1: On the Pi, `cd` to your `Interactive-Lab-Hub`, pull the updates from upstream (class lab-hub) and push the updates back to your own GitHub repo. You will need the personal access token for this.

```
pi@ixe00:~$ cd Interactive-Lab-Hub
pi@ixe00:~/Interactive-Lab-Hub $ git pull upstream Fall2022
pi@ixe00:~/Interactive-Lab-Hub $ git add .
pi@ixe00:~/Interactive-Lab-Hub $ git commit -m "get lab4 content"
pi@ixe00:~/Interactive-Lab-Hub $ git push
```

Option 2: On your your own GitHub repo, [create pull request](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2021Fall/readings/Submitting%20Labs.md) to get updates from the class Interactive-Lab-Hub. After you have latest updates online, go on your Pi, `cd` to your `Interactive-Lab-Hub` and use `git pull` to get updates from your own GitHub repo.

### Start brasinstorming ideas by reading: 
* [What do prototypes prototype?](https://www.semanticscholar.org/paper/What-do-Prototypes-Prototype-Houde-Hill/30bc6125fab9d9b2d5854223aeea7900a218f149)
* [Paper prototyping](https://www.uxpin.com/studio/blog/paper-prototyping-the-practical-beginners-guide/) is used by UX designers to quickly develop interface ideas and run them by people before any programming occurs. 
* [Cardboard prototypes](https://www.youtube.com/watch?v=k_9Q-KDSb9o) help interactive product designers to work through additional issues, like how big something should be, how it could be carried, where it would sit. 
* [Tips to Cut, Fold, Mold and Papier-Mache Cardboard](https://makezine.com/2016/04/21/working-with-cardboard-tips-cut-fold-mold-papier-mache/) from Make Magazine.
* [Surprisingly complicated forms](https://www.pinterest.com/pin/50032245843343100/) can be built with paper, cardstock or cardboard.  The most advanced and challenging prototypes to prototype with paper are [cardboard mechanisms](https://www.pinterest.com/helgangchin/paper-mechanisms/) which move and change. 
* [Dyson Vacuum Cardboard Prototypes](http://media.dyson.com/downloads/JDF/JDF_Prim_poster05.pdf)
<p align="center"><img src="https://dysonthedesigner.weebly.com/uploads/2/6/3/9/26392736/427342_orig.jpg"  width="200" > </p>

### Gathering materials for this lab:

* Cardboard (start collecting those shipping boxes!)
* Found objects and materials--like bananas and twigs.
* Cutting board
* Cutting tools
* Markers

(We do offer shared cutting board, cutting tools, and markers on the class cart during the lab, so do not worry if you don't have them!)

## Deliverables \& Submission for Lab 4

The deliverables for this lab are, writings, sketches, photos, and videos that show what your prototype:
* "Looks like": shows how the device should look, feel, sit, weigh, etc.
* "Works like": shows what the device can do.
* "Acts like": shows how a person would interact with the device.

For submission, the readme.md page for this lab should be edited to include the work you have done:
* Upload any materials that explain what you did, into your lab 4 repository, and link them in your lab 4 readme.md.
* Link your Lab 4 readme.md in your main Interactive-Lab-Hub readme.md. 
* Group members can turn in one repository, but make sure your Hub readme.md links to the shared repository.
* Labs are due on Mondays, make sure to submit your Lab 4 readme.md to Canvas.


## Lab Overview

A) [Capacitive Sensing](#part-a)

B) [OLED screen](#part-b) 

C) [Paper Display](#part-c)

D) [Materiality](#part-d)

E) [Servo Control](#part-e)

F) [Record the interaction](#part-f)

## The Report (Part 1: A-D, Part 2: E-F)

### Part A
### Capacitive Sensing, a.k.a. Human-Twizzler Interaction 

We want to introduce you to the [capacitive sensor](https://learn.adafruit.com/adafruit-mpr121-gator) in your kit. It's one of the most flexible input devices we are able to provide. At boot, it measures the capacitance on each of the 12 contacts. Whenever that capacitance changes, it considers it a user touch. You can attach any conductive material. In your kit, you have copper tape that will work well, but don't limit yourself! In the example below, we use Twizzlers--you should pick your own objects.


<p float="left">
<img src="https://cdn-learn.adafruit.com/guides/cropped_images/000/003/226/medium640/MPR121_top_angle.jpg?1609282424" height="150" />
<img src="https://cdn-shop.adafruit.com/1200x900/4401-01.jpg" height="150">
</p>

Plug in the capacitive sensor board with the QWIIC connector. Connect your Twizzlers with either the copper tape or the alligator clips (the clips work better). In this lab, we will continue to use the `circuitpython` virtual environment we created before. Activate `circuitpython` and `cd` to your Lab 4 folder to install the requirements by:

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ pip3 install -r requirements.txt
```

<img src="https://media.discordapp.net/attachments/679721816318803975/823299613812719666/PXL_20210321_205742253.jpg" width=400>
These Twizzlers are connected to pads 6 and 10. When you run the code and touch a Twizzler, the terminal will print out the following

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python cap_test.py 
Twizzler 10 touched!
Twizzler 6 touched!
```

### Part B
### More sensors

#### Light/Proximity/Gesture sensor (APDS-9960)

We here want you to get to know this awesome sensor [Adafruit APDS-9960](https://www.adafruit.com/product/3595). It is capable of sensing proximity, light (also RGB), and gesture! 

<img src="https://cdn-shop.adafruit.com/970x728/3595-03.jpg" width=200>

Connect it to your pi with Qwiic connector and try running the three example scripts individually to see what the sensor is capable of doing!

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python proximity_test.py
...
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python gesture_test.py
...
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python color_test.py
...
```

You can go the the [Adafruit GitHub Page](https://github.com/adafruit/Adafruit_CircuitPython_APDS9960) to see more examples for this sensor!

#### Rotary Encoder

A rotary encoder is an electro-mechanical device that converts the angular position to analog or digital output signals. The [Adafruit rotary encoder](https://www.adafruit.com/product/4991#technical-details) we ordered for you came with separated breakout board and encoder itself, that is, they will need to be soldered if you have not yet done so! We will be bringing the soldering station to the lab class for you to use, also, you can go to the MakerLAB to do the soldering off-class. Here is some [guidance on soldering](https://learn.adafruit.com/adafruit-guide-excellent-soldering/preparation) from Adafruit. When you first solder, get someone who has done it before (ideally in the MakerLAB environment). It is a good idea to review this material beforehand so you know what to look at.

<p float="left">
<img src="https://cdn-shop.adafruit.com/970x728/4991-01.jpg" height="200" />
<img src="https://cdn-shop.adafruit.com/970x728/377-02.jpg" height="200" />
<img src="https://cdn-shop.adafruit.com/970x728/4991-09.jpg" height="200">
</p>

Connect it to your pi with Qwiic connector and try running the example script, it comes with an additional button which might be useful for your design!

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python encoder_test.py
```

You can go to the [Adafruit Learn Page](https://learn.adafruit.com/adafruit-i2c-qt-rotary-encoder/python-circuitpython) to learn more about the sensor! The sensor actually comes with an LED (neo pixel): Can you try lighting it up? 

#### Joystick

A [joystick](https://www.sparkfun.com/products/15168) can be used to sense and report the input of the stick for it pivoting angle or direction. It also comes with a button input!

<p float="left">
<img src="https://cdn.sparkfun.com//assets/parts/1/3/5/5/8/15168-SparkFun_Qwiic_Joystick-01.jpg" height="200" />
</p>

Connect it to your pi with Qwiic connector and try running the example script to see what it can do!

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python joystick_test.py
```

You can go to the [SparkFun GitHub Page](https://github.com/sparkfun/Qwiic_Joystick_Py) to learn more about the sensor!

#### Distance Sensor

Earlier we have asked you to play with the proximity sensor, which is able to sense object within a short distance. Here, we offer [Qwiic Multi Distance Sensor](https://www.sparkfun.com/products/17072), which has a field of view of about 25° and is able to detect objects up to 3 meters away! 

<p float="left">
<img src="https://cdn.sparkfun.com//assets/parts/1/6/0/3/4/17072-Qwiic_Multi_Distance_Sensor_-_VL53L3CX-01.jpg" height="200" />
</p>

Connect it to your pi with Qwiic connector and try running the example script to see how it works!

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python distance_test.py
```

You can go to the [SparkFun GitHub Page](https://github.com/sparkfun/Qwiic_VL53L1X_Py) to learn more about the sensor and see other examples!

### Part C
### Physical considerations for sensing

Usually, sensors need to positioned in specific locations or orientations to make them useful for their application. Now that you've tried a bunch of the sensors, pick one that you would like to use, and an application where you use the output of that sensor for an interaction. For example, you can use a distance sensor to measure someone's height if you position it overhead and get them to stand under it.

**\*\*\*Draw 5 sketches of different ways you might use your sensor, and how the larger device needs to be shaped in order to make the sensor useful.\*\*\***

(1) Door Sensor for Pets

A design for pets to get back home by their own. 
![This is an image](https://github.com/Peggypei98/Interactive-Lab-Hub/blob/545c262d13c6eedcfcce575292ffac8d87470aa9/Lab%204/p1.jpg)

(2) Da Vinci Code

Guess a sepcific number!
![This is an image](https://github.com/Peggypei98/Interactive-Lab-Hub/blob/545c262d13c6eedcfcce575292ffac8d87470aa9/Lab%204/p2.jpg)

(3) Work-Out booster

A design helps counting your work-out amount, especiially for push-up and sit-up.
![This is an image](https://github.com/Peggypei98/Interactive-Lab-Hub/blob/545c262d13c6eedcfcce575292ffac8d87470aa9/Lab%204/p3.jpg)

(4) Volume Adjustment 

An application to adjust volume
![This is an image](https://github.com/Peggypei98/Interactive-Lab-Hub/blob/545c262d13c6eedcfcce575292ffac8d87470aa9/Lab%204/p4.jpg)

(5) A remote control for smart phone holders
![This is an image](https://github.com/Peggypei98/Interactive-Lab-Hub/blob/545c262d13c6eedcfcce575292ffac8d87470aa9/Lab%204/p5.jpg)

A design to adjust the position of smart phone holders

**\*\*\*What are some things these sketches raise as questions? What do you need to physically prototype to understand how to anwer those questions?\*\*\***

(1) Door Sensor for Pets

The proximity sensor we tested in Part B was a short-distance one, when a pet tried to get into a house, they might be trapped in the door. 


(2) Da Vinci Code

The number is ranging from 1 to 10 in the capacitive sensor, it would be too easy to get the answer.


(3) Work-Out booster

Sometimes the sensor is not that accurate. 


(4) Volume Adjustment 

A lack of joyful interaction between the design and users. We could add some features such as changing lights or showing different pictures on the display scrren.


(5) A remote control for smart phone holders

Same issue in (1). The sensor is a short-distance one, which means there would be a great chance that the sensor can't detect the movement.



**\*\*\*Pick one of these designs to prototype.\*\*\***

A prototype of our work-out counter

![This is an image](https://github.com/Peggypei98/Interactive-Lab-Hub/blob/545c262d13c6eedcfcce575292ffac8d87470aa9/Lab%204/p6.jpg)


### Part D
### Physical considerations for displaying information and housing parts


Here is an Pi with a paper faceplate on it to turn it into a display interface:

<img src="https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2020Fall/images/paper_if.png?raw=true"  width="250"/>


This is fine, but the mounting of the display constrains the display location and orientation a lot. Also, it really only works for applications where people can come and stand over the Pi, or where you can mount the Pi to the wall.

Here is another prototype for a paper display:

<img src="https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2020Fall/images/b_box.png?raw=true"  width="250"/>

Your kit includes these [SparkFun Qwiic OLED screens](https://www.sparkfun.com/products/17153). These use less power than the MiniTFTs you have mounted on the GPIO pins of the Pi, but, more importantly, they can be more flexibily be mounted elsewhere on your physical interface. The way you program this display is almost identical to the way you program a  Pi display. Take a look at `oled_test.py` and some more of the [Adafruit examples](https://github.com/adafruit/Adafruit_CircuitPython_SSD1306/tree/master/examples).

<p float="left">
<img src="https://cdn.sparkfun.com//assets/parts/1/6/1/3/5/17153-SparkFun_Qwiic_OLED_Display__0.91_in__128x32_-01.jpg" height="200" />
<img src="https://cdn.discordapp.com/attachments/679466987314741338/823354087105101854/PXL_20210322_003033073.jpg" height="200">
</p>


It holds a Pi and usb power supply, and provides a front stage on which to put writing, graphics, LEDs, buttons or displays.

This design can be made by scoring a long strip of corrugated cardboard of width X, with the following measurements:

| Y height of box <br> <sub><sup>- thickness of cardboard</sup></sub> | Z  depth of box <br><sub><sup>- thickness of cardboard</sup></sub> | Y height of box  | Z  depth of box | H height of faceplate <br><sub><sup>* * * * * (don't make this too short) * * * * *</sup></sub>|
| --- | --- | --- | --- | --- | 

Fold the first flap of the strip so that it sits flush against the back of the face plate, and tape, velcro or hot glue it in place. This will make a H x X interface, with a box of Z x X footprint (which you can adapt to the things you want to put in the box) and a height Y in the back. 

Here is an example:

<img src="https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2020Fall/images/horoscope.png?raw=true"  width="250"/>

Think about how you want to present the information about what your sensor is sensing! Design a paper display for your project that communicates the state of the Pi and a sensor. Ideally you should design it so that you can slide the Pi out to work on the circuit or programming, and then slide it back in and reattach a few wires to be back in operation.
 
**\*\*\*Sketch 5 designs for how you would physically position your display and any buttons or knobs needed to interact with it.\*\*\***

(1) Number Counter

A capacitive sensor display screen shows the total amount of the number. 
![This is an image](https://github.com/Peggypei98/Interactive-Lab-Hub/blob/9ea19ee0e2a93ddddabfccd73444da4778d85266/Lab%204/p7.jpg)



(2) Remote Volume Controller

An application to adjust volume with a screen display the dynamic status of the volume. 
![This is an image](https://github.com/Peggypei98/Interactive-Lab-Hub/blob/9ea19ee0e2a93ddddabfccd73444da4778d85266/Lab%204/p8.jpg)


(3) Safe distance detector

The device will detect whether the surrounding vehicles are too close to itself. If the distance is lower than a safe distacne, the color of the display will turn from green to red and notice the driver.
![This is an image](https://github.com/Peggypei98/Interactive-Lab-Hub/blob/9ea19ee0e2a93ddddabfccd73444da4778d85266/Lab%204/p9.jpg)


(4) Brightness sensor for eye care

THe device will detect the intensity of surrounding light. If the light isn't bright enough, the display screen will ask the user to turn on the light.
![This is an image](https://github.com/Peggypei98/Interactive-Lab-Hub/blob/9ea19ee0e2a93ddddabfccd73444da4778d85266/Lab%204/p10.jpg)


(5) Work-Out booster

A design helps counting your work-out amount, especiially for push-up and sit-up. The display screen will show the accumulated push-up and sit-up counts for users. 
![This is an image](https://github.com/Peggypei98/Interactive-Lab-Hub/blob/9ea19ee0e2a93ddddabfccd73444da4778d85266/Lab%204/p11.jpg)


**\*\*\*What are some things these sketches raise as questions? What do you need to physically prototype to understand how to anwer those questions?\*\*\***

(1) Number Counter

If the users press the button too fast, the sensor might has a hard time getting the value. 


(2) Remote Volume Controller

So far so good!


(3) Safe distance detector

The given sensor is a short-distance one, which means it might not sense correctly. 


(4) Brightness sensor for eye care

The brightness is very subjective to individuals, It was very hard to defined.


(5) Work-Out booster

We have tested the gesture sensor, yet the result was not that precise. 



**\*\*\*Pick one of these display designs to integrate into your prototype.\*\*\***

We pick the display design of number guessing as our prototype.
![This is an image](https://github.com/Peggypei98/Interactive-Lab-Hub/blob/9ea19ee0e2a93ddddabfccd73444da4778d85266/Lab%204/p12.jpg)


**\*\*\*Explain the rationale for the design.\*\*\*** (e.g. Does it need to be a certain size or form or need to be able to be seen from a certain distance?)

This design can be used in many place. If it is for playing games, we believe the size should be larger to engage participants. In contrast, if it is for password, we consider the size should be small, so the screen would not be able to be seen by other people.

Cardbord prototype of our design.
![This is an image](https://github.com/Peggypei98/Interactive-Lab-Hub/blob/b31a7e921ae2926e3b3f01218a8d3bf11085c510/Lab%204/p13.jpg)

![This is an image](https://github.com/Peggypei98/Interactive-Lab-Hub/blob/b31a7e921ae2926e3b3f01218a8d3bf11085c510/Lab%204/p14.jpg)



**\*\*\*Document your rough prototype.\*\*\***

This design can be simply used as a number guessing game or a door lock in daily life. The idea of this design is we use capacitive sensor to let users set their password. And next time they rotate the Rotary Encoder to the number so they can open the lock. While rotating the Rotary Encoder, the display screen will show whether it is correct.



LAB PART 2

### Part 2

Following exploration and reflection from Part 1, complete the "looks like," "works like" and "acts like" prototypes for your design, reiterated below.

### Part E (Optional)
### Servo Control with Joystick

In the class kit, you should be able to find the [Qwiic Servo Controller](https://www.sparkfun.com/products/16773) and [Micro Servo Motor SG51](https://www.adafruit.com/product/2201). The Qwiic Servo Controller will need external power supply to drive, which are included in your kit. Connect the servo controller to the miniPiTFT through qwiic connector and connect the external battery to the 2-Pin JST port (ower port) on the servo controller. Connect your servo to channel 2 on the controller, make sure the brown is connected to GND and orange is connected to PWM.

<img src="Servo_Setup.jpg" width="400"/>

In this exercise, we will be using the nice [ServoKit library](https://learn.adafruit.com/16-channel-pwm-servo-driver/python-circuitpython) developed by Adafruit! We will continue to use the `circuitpython` virtual environment we created. Activate the virtual environment and make sure to install the latest required libraries by running:

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ pip3 install -r requirements.txt
```

A servo motor is a rotary actuator or linear actuator that allows for precise control of angular or linear position. The position of a servo motor is set by the width of an electrical pulse, that is, we can use PWM (pulse-width modulation) to set and control the servo motor position. You can read [this](https://learn.adafruit.com/adafruit-arduino-lesson-14-servo-motors/servo-motors) to learn a bit more about how exactly a servo motor works.

Now that you have a basic idea of what a servo motor is, look into the script `qwiic_servo_example.py` we provide. In line 14, you should see that we have set up the min_pulse and max_pulse corresponding to the servo turning 0 - 180 degree. Try running the servo example code now and see what happens:

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python servo_test.py
```

It is also possible to control the servo using the sensors mentioned in as in part A and part B, and/or from some of the buttons or parts included in your kit, the simplest way might be to chain Qwiic buttons to the other end of the Qwiic OLED. Like this:

<p align="center"> <img src="chaining.png"  width="200" ></p>

You can then call whichever control you like rather than setting a fixed value for the servo. For more information on controlling Qwiic devices, Sparkfun has several python examples, such as [this](https://learn.sparkfun.com/tutorials/qwiic-joystick-hookup-guide/all#python-examples).

We encourage you to try using these controls, **while** paying particular attention to how the interaction changes depending on the position of the controls. For example, if you have your servo rotating a screen (or a piece of cardboard) from one position to another, what changes about the interaction if the control is on the same side of the screen, or the opposite side of the screen? Trying and retrying different configurations generally helps reveal what a design choice changes about the interaction -- _make sure to document what you tried_!

### Part F
### Record

Document all the prototypes and iterations you have designed and worked on! Again, deliverables for this lab are writings, sketches, photos, and videos that show what your prototype:

* __Feedbacks:__
  - Kaya: If the display screen can show the input result while guessing the password would be better. Overall, it's a good design. 
  - Kenny: I love the design, it's very interesting. I would like to have one in my dorm and play the Da Vinci Code game with my roommates. 

* __"Looks like": shows how the device should look, feel, sit, weigh, etc.__
  - We would like to design a cool interactive device that can act as a door lock and a number guessing game in daily life. 
  - We named our design "Da Vinci Code". 
  - The look of our design: it looks like a funny box which would be placed at the door or in the living room, its size is 38 cm, 28 cm, 28 cm, weight 315g.  

Here is a sketch of our design:
![This is an Image](https://github.com/Peggypei98/Interactive-Lab-Hub/blob/d0634110fa04677b94ab137678758c6fdfe379a5/Lab%204/pp1.jpg)
 

Here are the actual looks of our final design:

Front view:

We used a box as a frame to prototype our device. 
![This is an Image](https://github.com/Peggypei98/Interactive-Lab-Hub/blob/89f5c6c7d6a6dd653efc7c5ff510efc2c9dde09e/Lab%204/pp3.JPG)

Top view:

We use cardboard to make a place holding our Raspberry pi in the back. 
![This is an Image](https://github.com/Peggypei98/Interactive-Lab-Hub/blob/89f5c6c7d6a6dd653efc7c5ff510efc2c9dde09e/Lab%204/pp5.JPG)





* __"Works like": shows what the device can do__
  - Our device can work as a door lock in our daily life
    1. Set up a password by a user
    2. Press the rotate encode to confirm your password
    3. Next time, rotate the rotate encoder to input your password to open the lock
    4. If you input the correct password, the display screen will show "Correct password + (a cute bouncing ball)"
    5. If you input the wrong password, the display screen will show "Wrong password + (wihtout a ball)"
    6. Users can try guessing the password no more than 5 times


  - It can also be a number guessing game device
    1. One gamer set up a specific number and press the rotate encode to confirm her/his setting
    2. Other gamers can rotate the rotate encoder to input their answers
    3. If they input the correct guessing, the display screen will show "Correct password + (a cute bouncing ball)"
    4. If they input the wrong guessing, the display screen will show "Wrong password + (without a ball)"
    5. Each gamers has one chance in every round of the game. 



* __"Acts like": shows how a person would interact with the device__

Here is a demo video that shows how our device acts like:
[![IMAGE ALT TEXT HERE](https://github.com/Peggypei98/Interactive-Lab-Hub/blob/1f5254f523a1bfaa92be18163309e064a0c5bb98/Lab%204/pp6.JPG)](https://youtu.be/olkPlY-2KlY)

Our code:
https://github.com/Peggypei98/Interactive-Lab-Hub/blob/1f5254f523a1bfaa92be18163309e064a0c5bb98/Lab%204/lab4.py



