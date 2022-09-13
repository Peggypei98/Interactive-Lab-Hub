import time
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789


import digitalio
import board
from PIL import Image, ImageDraw
import adafruit_rgb_display.ili9341 as ili9341
import adafruit_rgb_display.st7789 as st7789  # pylint: disable=unused-import
import adafruit_rgb_display.hx8357 as hx8357  # pylint: disable=unused-import
import adafruit_rgb_display.st7735 as st7735  # pylint: disable=unused-import
import adafruit_rgb_display.ssd1351 as ssd1351  # pylint: disable=unused-import
import adafruit_rgb_display.ssd1331 as ssd1331  # pylint: disable=unused-import


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


# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
font1 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 24)
font2 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 40)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

# Set buttom
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()


x1 = 0
x2 = 0
y1=5
y2=30

def clockWise():
    # Draw a black filled box to clear the image.
    global x1, x2, y1, y2    
    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    if x1 < 130 and x2 < 130 and y1 == 5 and y2 == 30:
        x1 += 10
        x2 += 10
    elif y1 < 70 and y2 < 95 and x1 == 130 and x2 == 130:
        y1 += 5
        y2 += 5
    elif y1 == 70 and y2 == 95 and x1 > 0 and x2 > 0:
        x1 -= 10
        x2 -= 10
    elif x1 == 0 and x2 == 0 and y1 <= 70 and y2 <= 95:
        y1 -= 5
        y2 -= 5

    #TODO: fill in here. You should be able to look in cli_clock.py and stats.py
    draw.text((x1,y1), time.strftime("%a %d" ), font=font1, fill="#FFFF9C")
    draw.text((x2,y2), time.strftime("%H:%M"), font=font2, fill="#AEFF9C")

def counterClockWise():
    # Draw a black filled box to clear the image.
    global x1, x2, y1, y2    
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    if x1 == 0 and x2 == 0 and y1 < 70 and y2 < 95:
        y1 += 5
        y2 += 5
    elif y1 == 70 and y2 == 95 and x1 < 130 and x2 < 130:
        x1 += 10
        x2 += 10
    elif x1 <= 130 and x2 <= 130 and y1 == 0 and y2 == 25:
        x1 -= 10
        x2 -= 10
    elif y1 <= 70 and y2 <= 95 and x1 == 130 and x2 == 130:
        y1 -= 5
        y2 -= 5


    #TODO: fill in here. You should be able to look in cli_clock.py and stats.py
    draw.text((x1,y1), time.strftime("%a %d" ), font=font1, fill="#9CD9FF")
    draw.text((x2,y2), time.strftime("%H:%M"), font=font2, fill="#FF9CDB")

def sun():
    # Configuration for CS and DC pins (these are PiTFT defaults):
    cs_pin = digitalio.DigitalInOut(board.CE0)
    dc_pin = digitalio.DigitalInOut(board.D25)
    reset_pin = digitalio.DigitalInOut(board.D24)

    BAUDRATE = 24000000

    spi = board.SPI()


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
    # pylint: enable=line-too-long

    # Create blank image for drawing.
    # Make sure to create image with mode 'RGB' for full color.
    if disp.rotation % 180 == 90:
        height = disp.width  # we swap height/width to rotate it to landscape!
        width = disp.height
    else:
        width = disp.width  # we swap height/width to rotate it to landscape!
        height = disp.height
    image = Image.new("RGB", (width, height))


    import PIL.Image

    # Get drawing object to draw on image.
    draw = ImageDraw.Draw(image)

    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
    disp.image(image)

    image1 = Image.open("sun1.jpg")
    image = image1.convert('RGBA')

    backlight = digitalio.DigitalInOut(board.D22)
    backlight.switch_to_output()
    backlight.value = True


    # Scale the image to the smaller screen dimension
    image_ratio = image.width / image.height
    screen_ratio = width / height
    if screen_ratio < image_ratio:
        scaled_width = image.width * height // image.height
        scaled_height = height
    else:
        scaled_width = width
        scaled_height = image.height * width // image.width
    image = image.resize((scaled_width, scaled_height), Image.BICUBIC)

    # Crop and center the image
    x = scaled_width // 2 - width // 2
    y = scaled_height // 2 - height // 2
    image = image.crop((x, y, x + width, y + height))

    # Display image.
    disp.image(image)

def moon():
    # Configuration for CS and DC pins (these are PiTFT defaults):
    cs_pin = digitalio.DigitalInOut(board.CE0)
    dc_pin = digitalio.DigitalInOut(board.D25)
    reset_pin = digitalio.DigitalInOut(board.D24)

    BAUDRATE = 24000000

    spi = board.SPI()


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
    # pylint: enable=line-too-long

    # Create blank image for drawing.
    # Make sure to create image with mode 'RGB' for full color.
    if disp.rotation % 180 == 90:
        height = disp.width  # we swap height/width to rotate it to landscape!
        width = disp.height
    else:
        width = disp.width  # we swap height/width to rotate it to landscape!
        height = disp.height
    image = Image.new("RGB", (width, height))


    import PIL.Image

    # Get drawing object to draw on image.
    draw = ImageDraw.Draw(image)

    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
    disp.image(image)

    image1 = Image.open("moon1.jpg")
    image = image1.convert('RGBA')

    backlight = digitalio.DigitalInOut(board.D22)
    backlight.switch_to_output()
    backlight.value = True


    # Scale the image to the smaller screen dimension
    image_ratio = image.width / image.height
    screen_ratio = width / height
    if screen_ratio < image_ratio:
        scaled_width = image.width * height // image.height
        scaled_height = height
    else:
        scaled_width = width
        scaled_height = image.height * width // image.width
    image = image.resize((scaled_width, scaled_height), Image.BICUBIC)

    # Crop and center the image
    x = scaled_width // 2 - width // 2
    y = scaled_height // 2 - height // 2
    image = image.crop((x, y, x + width, y + height))

    # Display image.
    disp.image(image)





while True:
    if not buttonA.value:
        sun()
    if not buttonB.value:
        moon()
    # Display image.
    disp.image(image, rotation)
    time.sleep(0.01)
Footer

