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

ctx.rectangle(0, 0, 1, 1)  # Rectangle(x0, y0, x1, y1)
ctx.set_source(pat)
ctx.fill()


image_folder = "image_" + str(datetime.now()).replace(' ','_')[-6:]
os.makedirs(image_folder)

file_drawing = open(image_folder + '/draw_instr.txt', 'x')
#ctx.translate(0.1, 0.1)  # Changing the current transformation matrix

#ctx.move_to(0.1, 0.1)
# Arc(cx, cy, radius, start_angle, stop_angle)
#ctx.arc(0.2, 0.2, 0.1, math.pi, 0)
#ctx.arc(0.4 , 0.2, 0.1, math.pi, 0)
curves_drawn = stats.randint.rvs(3, 50)
file_drawing.write(str(curves_drawn) + '\n')
for n in range(curves_drawn):
    
    x_rands, y_rands = stats.uniform.rvs(size = (2, 5))
    
    ctx.move_to(x_rands[0], y_rands[0])
    ctx.line_to(x_rands[1], y_rands[1])
    ctx.line_to(x_rands[2], y_rands[2])
    
    ctx.curve_to(x_rands[3], y_rands[3],
             x_rands[4], y_rands[4],
             x_rands[0], y_rands[0])
    # ctx.close_path()
    col_rands = stats.uniform.rvs(0.3, 0.6, size = 3)
    col_rands[0] = 0.8
    ctx.set_source_rgb(*col_rands)  # Solid color
    ctx.set_line_width(0.015)
    ctx.stroke()
    
    file_drawing.write(str(n) + '\n')
    file_drawing.writelines(str(x_rands) + '\n')
    file_drawing.writelines(str(y_rands) + '\n')
    file_drawing.writelines(str(col_rands) + '\n')
    surface.write_to_png(image_folder + 
                         '/rand_img_'+ 
                         str(n)+
                         '.png')  # Output to PNG

file_drawing.close()
