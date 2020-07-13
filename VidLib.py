# Helper library for common video editing tasks

import cv2
import os
from PIL import Image, ImageFont, ImageDraw
import numpy
import random

video = None
cursize = None
curbg = None
img = None
pixels = None
font = None

def create(name='video.avi', size=500, bg='white', fps=30, fontsize=16):
  global video, cursize, curbg, img, pixels, font
  font = ImageFont.truetype("./resources/DejaVuSans.ttf", fontsize)
  cursize = size
  curbg = bg
  video = cv2.VideoWriter(name, 0, fps, (size,size))
  img = Image.new('RGB', (size, size), color = bg)
  pixels = img.load()

def text(text, x = 0, y = 0, color = (0,0,0)):
  global img, font
  ImageDraw.Draw(img).text((x,y), text, color, font=font)

def next(bg=None):
  global video, cursize, curbg, img, pixels
  if bg == None:
      bg = curbg
  else:
      curbg = bg
  open_cv_image = numpy.array(img)
  open_cv_image = open_cv_image[:, :, ::-1].copy() # RGB Fix
  video.write(open_cv_image)
  img = Image.new('RGB', (cursize, cursize), color = curbg)
  pixels = img.load()

def done():
  global video
  video.release()
