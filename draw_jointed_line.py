# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 21:21:07 2021

@author: Nero
"""

# draw_line.py
from PIL import Image, ImageDraw

def line(output_path):
    image = Image.new("RGB", (1270, 850), "red")
    points = [(100, 100), (150, 200), (200, 50), (400, 400)]
    draw = ImageDraw.Draw(image)
    draw.line(points, width=15, fill="green", joint="curve")
    image.save(output_path)
if __name__ == "__main__":
    line("jointed_lines.jpg")
