import time
import board
import busio

import adafruit_mpr121

i2c = busio.I2C(board.SCL, board.SDA)

mpr121 = adafruit_mpr121.MPR121(i2c)


###############################################################

# SPDX-FileCopyrightText: 2021 John Furcean
# SPDX-License-Identifier: MIT

"""I2C rotary encoder simple test example."""

import board
from adafruit_seesaw import seesaw, rotaryio, digitalio

# For use with the STEMMA connector on QT Py RP2040
# import busio
# i2c = busio.I2C(board.SCL1, board.SDA1)
# seesaw = seesaw.Seesaw(i2c, 0x36)

seesaw = seesaw.Seesaw(board.I2C(), addr=0x36)

seesaw_product = (seesaw.get_version() >> 16) & 0xFFFF
print("Found product {}".format(seesaw_product))
if seesaw_product != 4991:
    print("Wrong firmware loaded?  Expected 4991")

seesaw.pin_mode(24, seesaw.INPUT_PULLUP)
button = digitalio.DigitalIO(seesaw, 24)
button_held = False

encoder = rotaryio.IncrementalEncoder(seesaw)
last_position = None

###############################################################

# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import board
import busio
import adafruit_ssd1306
from PIL import Image, ImageDraw, ImageFont
from PIL import Image, ImageDraw, ImageFont

# Create the I2C interface.
i2c = busio.I2C(board.SCL, board.SDA)

# Create the SSD1306 OLED class.
# The first two parameters are the pixel width and pixel height.  Change these
# to the right size for your display!
oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)


# Helper function to draw a circle from a given position with a given radius
# This is an implementation of the midpoint circle algorithm,
# see https://en.wikipedia.org/wiki/Midpoint_circle_algorithm#C_example for details
def draw_circle(xpos0, ypos0, rad, col=1):
    x = rad - 1
    y = 0
    dx = 1
    dy = 1
    err = dx - (rad << 1)
    while x >= y:
        oled.pixel(xpos0 + x, ypos0 + y, col)
        oled.pixel(xpos0 + y, ypos0 + x, col)
        oled.pixel(xpos0 - y, ypos0 + x, col)
        oled.pixel(xpos0 - x, ypos0 + y, col)
        oled.pixel(xpos0 - x, ypos0 - y, col)
        oled.pixel(xpos0 - y, ypos0 - x, col)
        oled.pixel(xpos0 + y, ypos0 - x, col)
        oled.pixel(xpos0 + x, ypos0 - y, col)
        if err <= 0:
            y += 1
            err += dy
            dy += 2
        if err > 0:
            x -= 1
            dx += 2
            err += dx - (rad << 1)


# initial center of the circle
center_x = 63
center_y = 15
# how fast does it move in each direction
x_inc = 1
y_inc = 1
# what is the starting radius of the circle
radius = 8

# start with a blank screen
oled.fill(0)
# we just blanked the framebuffer. to push the framebuffer onto the display, we call show()
oled.show()

###############################################################


setpassword = []

while True:
    if not button.value and not button_held:
        button_held = True
        print("Finish setting password")
        print('setpassword: ', setpassword)
        break

    for i in range(10):
        if mpr121[i].value:
            print(f"Twizzler {i} touched!")
            setpassword.append(i)

    time.sleep(0.25)  # Small delay to keep from spamming output messages.


trypassword = []
Guess_status = False
attempts = 5

while True:
    
    if attempts == 0:
        # Create blank image for drawing.
        image = Image.new("1", (oled.width, oled.height))
        draw = ImageDraw.Draw(image)

        # Load a font in 2 different sizes.
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)

        # Draw the text
        draw.text((0, 8), "Game Over!!!", font=font, fill=255)

        # Display image
        oled.image(image)
        oled.show()

        break

    

    # negate the position to make clockwise rotation positive
    position = -encoder.position

    if len(trypassword) == len(setpassword):
        Guess_status = True

    if position != last_position:
        last_position = position
        print("Position: {}".format(position))

    if not button.value and not button_held:
        button_held = True
        trypassword.append(position)
        print(f"Guess password {position}")
        print('trypassword', trypassword)

    if button.value and button_held:
        button_held = False
        print("Button released")


    if Guess_status == False:
        # Create blank image for drawing.
        image = Image.new("1", (oled.width, oled.height))
        draw = ImageDraw.Draw(image)

        # Load a font in 2 different sizes.
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 14)

        # Draw the text
        draw.text((0, 8), f"{len(setpassword)} digit password", font=font, fill=255)
        # draw.text((0, 30), "Hello!", font=font2, fill=255)
        # draw.text((34, 46), "Hello!", font=font2, fill=255)

        # Display image
        oled.image(image)
        oled.show()

    
    else:
       

        if trypassword == setpassword:
            # undraw the previous circle
            draw_circle(center_x, center_y, radius, col=0)

            # if bouncing off right
            if center_x + radius >= oled.width:
                # start moving to the left
                x_inc = -1
            # if bouncing off left
            elif center_x - radius < 0:
                # start moving to the right
                x_inc = 1

            # if bouncing off top
            if center_y + radius >= oled.height:
                # start moving down
                y_inc = -1
            # if bouncing off bottom
            elif center_y - radius < 0:
                # start moving up
                y_inc = 1

            # go more in the current direction
            center_x += x_inc
            center_y += y_inc

            # draw the new circle
            draw_circle(center_x, center_y, radius)
            # show all the changes we just made
            oled.show()

            # Create blank image for drawing.
            image = Image.new("1", (oled.width, oled.height))
            draw = ImageDraw.Draw(image)

            # Load a font in 2 different sizes.
            font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 14)

            # Draw the text
            draw.text((0, 8), "Correct Password!", font=font, fill=255)

            # Display image
            oled.image(image)
            oled.show()

        else:
            # Create blank image for drawing.
            image = Image.new("1", (oled.width, oled.height))
            draw = ImageDraw.Draw(image)

            # Load a font in 2 different sizes.
            font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 14)

            # Draw the text
            draw.text((0, 0), "Wrong Password!", font=font, fill=255)
            draw.text((0, 15), f"{attempts - 1} attempts left!", font=font, fill=255)

            # Display image
            oled.image(image)
            oled.show()

            trypassword.clear()
            Guess_status == False
            trypassword = []


