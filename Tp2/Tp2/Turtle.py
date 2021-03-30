#Turtle.py

import math


def _line2svg(x1, y1, x2, y2, stroke, color):
    svgline = "<line x1=""{0}"" y1=""{1}"" x2=""{2}"" y2=""{3}"" ""style=""stroke:rgb({4},{5},{6});stroke-width:{7}"" />"
    return svgline.format(x1, y1, x2, y2, color[0], color[1], color[2], stroke)


class Turtle:

    def __init__(self):
        self.x = 500
        self.y = 500
        self.stroke = 1
        self.deg = 90
        self.color = (0, 0, 0)
        self.lines = []

    def save(self, filename):
        fh = open(filename, mode="w+")
        with fh:
            print("<!DOCTYPE html>\n<html>\n<body>\n", file=fh)
            print("<svg height=""1000"" width=""1000"">", file=fh)
            for x in self.lines:
                print(_line2svg(*x), file=fh)
            print("</svg>\n</body>\n</html>\n", file=fh)

    def forward(self, len):
        x2 = self.x + math.sin(math.radians(self.deg)) * len
        y2 = self.y + math.cos(math.radians(self.deg)) * len
        self.lines.append([self.x, self.y, x2, y2, self.stroke, self.color])
        self.x, self.y = x2 , y2

    def back(self, len):
        newdeg = self.deg + 180
        if newdeg > 360:
            newdeg = newdeg - 360
        x2 = self.x + math.sin(math.radians(newdeg)) * len
        y2 = self.y + math.cos(math.radians(newdeg)) * len
        self.lines.append([self.x, self.y, x2, y2, self.stroke, self.color])
        self.x, self.y = x2, y2

    def right(self, deg):
        newdeg = self.deg + deg
        if newdeg > 360:
            newdeg = newdeg - 360
        self.deg = newdeg

    def left(self, deg):
        newdeg = self.deg + deg
        if newdeg < 0:
            newdeg = newdeg + 360
        self.deg = newdeg

    def setx(self, x):
        x2 = x
        y2 = self.y
        self.lines.append([self.x, self.y, x2, y2, self.stroke, self.color])
        self.x, self.y = x2, y2

    def sety(self, y):
        x2 =self.x
        y2 = y
        self.lines.append([self.x, self.y, x2, y2, self.stroke, self.color])
        self.x, self.y = x2, y2

    def setxy(self, x, y):
        x2 = x
        y2 = y
        self.lines.append([self.x, self.y, x2, y2, self.stroke, self.color])
        self.x, self.y = x2, y2

    def setpos(self, x, y):
        x2 = x
        y2 = y
        self.lines.append([self.x, self.y, x2, y2, self.stroke, self.color])
        self.x, self.y = x2, y2

    def pendown(self):
        x = 2
        self.stroke = x

    def penup(self):
        x = 0
        self.stroke = x

    def setpencolor(self, color):
        self.color = color

    def home(self):
        x2 = 500
        y2 = 500
        self.lines.append([self.x, self.y, x2, y2, self.stroke, self.color])
        self.x, self.y = x2, y2