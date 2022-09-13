import time
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
from time import strftime, sleep
import adafruit_rgb_display.st7789 as st7789

# Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 64000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

# Create the ST7789 display:
disp = st7789.ST7789(
    spi,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
)

# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for full color.
height = disp.width  # we swap height/width to rotate it to landscape!
width = disp.height
image = Image.new("RGB", (width, height))
rotation = 90

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
disp.image(image, rotation)
# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)
timeSize= 50
fontTime = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", timeSize)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

image1 = Image.open("sun.png")
image_ratio = image1.width / image1.height
screen_ratio = width / height
if screen_ratio < image_ratio:
    scaled_width = image1.width * height // image1.height
    scaled_height = height
else:
    scaled_width = scaled_height = image1.width // 15
image1 = image1.resize((scaled_width, scaled_height), Image.BICUBIC)
disp.image(image1)

image2 = Image.open("moon.png")
image_ratio = image2.width / image2.height
screen_ratio = width / height
if screen_ratio < image_ratio:
    scaled_width = image2.width * height // image2.height
    scaled_height = height
else:
    scaled_width = width
    scaled_height = image2.height * width // image2.width
image2 = image2.resize((scaled_width, scaled_height), Image.BICUBIC)
disp.image(image2)


while True:
    # Draw a black filled box to clear the image.
    #TODO: Lab 2 part D work should be filled in here. You should be able to look in cli_clock.py and stats.py  
    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    

    date = strftime("%m/%d/%Y")
    nowhours = strftime("%H")
    nowmins = strftime("%M")
    nowsec = strftime("%S")
    nowtime = nowhours + ":" + nowmins + ":" + nowsec
   
    print (date+" "+nowtime, end="", flush=True)
    print("\r", end="", flush=True)
    date = "Date: " + date
    
    
    y = top
    draw.text((x, y), date, font=font, fill="#FFFFFF")

    y += font.getsize(date)[1]
    nowhours = int(nowhours)
    if nowhours in range(5, 17): #morning+afternoon
        draw.text((x, y), nowtime, font=font, fill="#f6faa7")
    elif nowhours in range(17, 24) or (0, 5):
        draw.text((x, y), time, font=fontTime, fill="#405f91")

    
    # Display image.
    disp.image(image, rotation)
    if nowhours in range(5,17):
        disp.image(image1)
    else:
        disp.image(image2)


    sleep(1)   












   
