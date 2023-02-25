# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 16:06:16 2021

@author: Nero
"""

#!/usr/bin/env python

import math
import cairo
import scipy.stats as stats
import os
from datetime import datetime
import numpy as np

WIDTH, HEIGHT = 1024, 1024

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context(surface)

ctx.scale(WIDTH, HEIGHT)  # Normalizing the canvas

pat = cairo.LinearGradient(0.0, 0.0, 1.0, 1.0) # should fit in rectangle below
pat.add_color_stop_rgba(0.4, 0.9, 0.1, 0.1, 0.5)  # First stop, 50% opacity
pat.add_color_stop_rgba(0.78, 0.3, 0.1, 0.8, 0.5)  # Last stop, 100% opacity

ctx.rectangle(0, 0, 1, 1)  # Rectangle(x0, y0, x1, y1)
ctx.set_source(pat)
ctx.fill()

pat = cairo.RadialGradient(0.4, 0.35, 0.25, 0.6, 0.5, 0.1) # should fit in rectangle below
pat.add_color_stop_rgba(0.8, 0.6, 0.3, 0.1, 0.5)  # First stop, 50% opacity
pat.add_color_stop_rgba(0.43, 0, 1, 0.8, 0.5)  # Last stop, 100% opacity

ctx.set_source(pat)
ctx.fill()

surface.write_to_png('rand_img_'+
                          '.png')
