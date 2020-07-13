import sys
sys.path.insert(0, '..')

import VidLib
import random

maxc = 1000
l = [(255,255,255)]*501
VidLib.create(size=500, fps=30, bg=(255,0,0))

for count in range(maxc):
  r = random.randint(0,255)
  g = random.randint(0,255)
  b = random.randint(0,255)
  l[500] = (r, g, b)
  for y in range(500):
    for x in range(500):
      VidLib.pixels[x,y] = l[y]
    l[y] = l[y + 1]
  
  if count > 510:
    VidLib.text("!!!PARTY HARD!!!", color=(g,r,b))
  elif count > 470:
    VidLib.text("Oh well, guess I'll join them")
  elif count > 400:
    VidLib.text("They are almost here!")
  else:
    VidLib.text("HELP")
  print("Progress: " + str(count) + "/" + str(maxc))
  VidLib.next()

VidLib.done()

