#!/usr/bin/env python

import math
from reportlab.lib.pagesizes import letter, A1
from reportlab.pdfgen import canvas
from reportlab.lib.colors import Color
from reportlab.lib.units import mm

canvas = canvas.Canvas("test.pdf", pagesize=A1)
width, height = A1
lwidth, lheight = letter


font_size = 4 * mm
scale = 10 * mm
line_len = 40 * mm

grid_color = Color(0, 0 , 0, alpha=0.4)
canvas.setFillColor(grid_color)
canvas.setStrokeColor(grid_color)

# Generate Grid
for x in range(math.ceil(width / lwidth)):
    for y in range(math.ceil(height / lheight)):
        canvas.circle(x * lwidth, y * lheight, 20 * mm, stroke=1, fill=0)

        canvas.line(
            x * lwidth - line_len / 2,
            y * lheight + lheight / 2,
            x * lwidth + line_len / 2,
            y * lheight + lheight / 2,
        )
        canvas.line(
            x * lwidth + lwidth / 2,
            y * lheight - line_len / 2,
            x * lwidth + lwidth / 2,
            y * lheight + line_len / 2,
        )

        canvas.setFont("Courier", font_size)

        for i in range(-1, 2, 2):
            for j in range(-1, 2, 2):
                canvas.drawCentredString(
                    x * lwidth + i * scale,
                    y * lheight + j * scale - font_size / 4,
                    "{}{}".format(x, y),
                )


design_color = Color(0, 0 , 0, alpha=1)
canvas.setFillColor(design_color)
canvas.setStrokeColor(design_color)
canvas.circle(300 * mm, 300 * mm, 250* mm, stroke=1, fill=0)


canvas.save()
