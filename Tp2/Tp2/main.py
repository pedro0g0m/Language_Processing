# main.py

from Parser import Parser

with open("test.txt", mode="r") as fh:
    contents = fh.read()

parser = Parser()
parser.Parse(contents)

parser.turtle.save("ola.html")

