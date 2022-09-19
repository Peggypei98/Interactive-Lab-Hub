import time
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
from time import strftime, sleep
import adafruit_rgb_display.st7789 as st7789
import adafruit_rgb_display.hx8357 as hx8357  # pylint: disable=unused-import
import adafruit_rgb_display.st7735 as st7735  # pylint: disable=unused-import
import adafruit_rgb_display.ssd1351 as ssd1351  # pylint: disable=unused-import
import adafruit_rgb_display.ssd1331 as ssd1331  # pylint: disable=unused-import
import adafruit_rgb_display.ili9341 as ili9341

# Get UV index: https://github.com/bachya/pyopenuv/

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
draw.rectangle((1, 0, width, height), outline=0, fill=(0, 0, 0))
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
timeSize= 40
suntSize =20
fontTime = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", timeSize)
fontSunt = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", suntSize)


# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

# Sunrise and sunset time : https://stackoverflow.com/questions/38986527/sunrise-and-sunset-time-in-python
import datetime
from suntime import Sun, SunTimeException

# The house at Cornell Tech
latitude = 40.76
longitude = -73.95

sun = Sun(latitude, longitude)

# Get today's sunrise and sunset in UTC
today_sr = sun.get_sunrise_time()
today_ss = sun.get_sunset_time()
sunrise_h = int(today_sr.strftime("%H"))-4
sunrise_m = int(today_sr.strftime("%M"))
sunset_h = int(today_ss.strftime("%H"))-4
sunset_m = int(today_ss.strftime("%M"))


print('Today at Cornell Tech the sun raised at {} and get down at {} UTC'.
      format(today_sr.strftime('%H:%M'), today_ss.strftime('%H:%M')))


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

    image1 = Image.open("sunrise.jpg")
    image = image1.convert('RGB')

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

    image1 = Image.open("sunset.jpg")
    image = image1.convert('RGB')

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

# On a special date in your machine's local time zone
#abd = datetime.date(2014, 10, 3)
#abd_sr = sun.get_local_sunrise_time(abd)
#abd_ss = sun.get_local_sunset_time(abd)
#print('On {} the sun at Warsaw raised at {} and get down at {}.'.
      #format(abd, abd_sr.strftime('%H:%M'), abd_ss.strftime('%H:%M')))

# strftime: https://www.geeksforgeeks.org/python-strftime-function/#:~:text=The%20strftime()%20function%20is,and%20returns%20the%20string%20representation.&text=Returns%20%3A%20It%20returns%20the%20string,the%20date%20or%20time%20object.

#image1 = Image.open("sunrise.jpg")
#scaled_width = scaled_height = image1.width // 300
#image1 = image1.resize((scaled_width, scaled_height), Image.BICUBIC)
#disp.image(image1)

#image2 = Image.open("sunset.jpg")
#scaled_width = scaled_height = image2.width // 150
#image2 = image2.resize((scaled_width, scaled_height), Image.BICUBIC)
#disp.image(image2)





while True:
    # Draw a black filled box to clear the image.
    #TODO: Lab 2 part D work should be filled in here. You should be able to look in cli_clock.py and stats.py  
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    
    date = strftime("%m/%-d/%Y")
    nowweekday = strftime("%a")
    nowhours = strftime("%H")
    nowmins = strftime("%M")
    nowsec = strftime("%S")
    nowtime = nowhours + ":" + nowmins + ":" + nowsec
   
    print (date+" "+nowweekday+" "+nowtime, end="", flush=True)
    print("\r", end="", flush=True)
    date_f = "Date: " + date + " "+ nowweekday
    
    sunrise = str(sunrise_h) + ":" +str(sunrise_m)
    sunset = str(sunset_h) + ":" +str(sunset_m)

    y = top
    draw.text((x, y), date_f, font=font, fill="#FFFFFF")
    y += font.getsize(date_f)[1]+15
    nowhours = int(nowhours)
    if nowhours in range(0,6): #midnight
        draw.text((x,y), nowtime, font=fontTime, fill="#340a52")
    elif nowhours in range(6,13): #morning
        draw.text((x,y), nowtime, font=fontTime, fill="#f0e630")
    elif nowhours in range(13,18): #afternoon
        draw.text((x,y), nowtime, font=fontTime, fill="#f08d30")
    elif nowhours in range(18,24): #night
        draw.text((x,y), nowtime, font=fontTime, fill="#237bd9")
    y += font.getsize(nowtime)[1]
    draw.text((65, 110), sunrise, font=fontSunt, fill="#f5da2c")
    y += font.getsize(sunrise)[1]
    draw.text((175, 110), sunset, font=fontSunt, fill="#f57c2c")

    if not buttonA.value:
        sun()
    if not buttonB.value:
        moon()

    
    # Display image.
    #disp.image(image1, rotation)
    #disp.image(image2, rotation)
    #if nowhours in range(5,17):
        #disp.image(image1,rotation)
    #else:
        # disp.image(image2,rotation)

 # Display image.
    disp.image(image, rotation)
    time.sleep(0.1)










