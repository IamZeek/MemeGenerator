import json
import random
import textwrap

from PIL import Image, ImageDraw, ImageFont
import os

f = open("jokes.json")
data = json.load(f)
f.close()
end = len(data)
number = random.randint(1,end)
data_random = data[number]

line_one = data_random["setup"]
line_two = data_random["punchline"]
line_one = line_one.upper()
line_two = line_two.upper()

dir_path = os.path.dirname(os.path.abspath(__file__))
_,_, file = next(os.walk(dir_path + "\Images"))
no_img = len(file)
rand_img_no = random.randint(1,no_img)
im = Image.open("Images/Funny("+str(rand_img_no)+").jpg")
draw = ImageDraw.Draw(im)
image_width,image_height = im.size
if (image_width < image_height):
    font = ImageFont.truetype(font="BRLNSB.TTF", size= int(image_width/10))
else:
    font = ImageFont.truetype(font="BRLNSB.TTF", size= int(image_height/10))

char_width, char_height = font.getsize("A")
chars_per_line = image_width / char_width
top_line = textwrap.wrap(line_one,width=int(chars_per_line))
bottom_line = textwrap.wrap(line_two,width=int(chars_per_line))

#Line 1 positioning
lo_y = 10
for line in top_line:
    line_width , line_height = font.getsize(line)
    lo_x = (image_width - line_width)/2
    draw.text((lo_x,lo_y),line,fill="white",font=font)
    lo_y += line_height

#Line 2 positioning
lt_y = image_height - char_height * len (bottom_line) - 15
for line in bottom_line:
    line_width , line_height = font.getsize(line)
    lt_x = (image_width - line_width)/2
    draw.text((lt_x,lt_y),line,fill="white",font=font)
    lt_y += line_height

im.show()
