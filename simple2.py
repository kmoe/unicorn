#!/usr/bin/env python

import unicornhat as UH
import time

for y in range(8):
  for x in range(8):
    UH.set_pixel(x,y,255,255,255)
    UH.show()
    time.sleep(0.0005)

time.sleep(1)
