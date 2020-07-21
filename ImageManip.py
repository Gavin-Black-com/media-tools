from PIL import Image, ImageFont, ImageDraw
import numpy


def greyscale_img (loc):
    img = Image.open(loc)
    pixels = list(img.getdata())
    return [ (x+y+z)/(255.0*3) for (x,y,z,w) in pixels]

