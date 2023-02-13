from traceback import format_tb
from PIL import Image

ascii_char = ' .:-=+*#%@'


with Image.open("Screenshot from 2022-01-17 04-26-30.png") as img:
    img = img.resize((500, 500))


    for y in range(img.height):
        line = ""
        for x in range(img.width):
            rgb = img.getpixel((x, y))
            grey = sum(rgb) // len(rgb)
            index = grey * 9 // 255
            line += ascii_char[index] + " " 
        print(line)
            
