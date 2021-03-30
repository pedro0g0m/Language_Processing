# Command.py
from Turtle import Turtle


def do_forward(command, parser):
    p1 = command.args['len']
    parser.turtle.forward(p1)


def do_back(command, parser):
    p1 = command.args['len']
    parser.turtle.back(p1)


def do_left(command, parser):
    p1 = command.args['deg']
    parser.turtle.left(p1)


def do_right(command, parser):
    p1 = command.args['deg']
    parser.turtle.right(p1)


def do_setpos(command, parser):
    p1 = command.args['coordinate'][0]
    p2 = command.args['coordinate'][1]
    parser.turtle.setpos(p1, p2)

def do_setxy(command, parser):
    p1 = command.args['coordinate'][0]
    p2 = command.args['coordinate'][1]
    parser.turtle.setxy(p1, p2)


def do_setx(command, parser):
    p1 = command.args['x']
    parser.turtle.setx(p1)


def do_sety(command, parser):
    p1 = command.args['y']
    parser.turtle.sety(p1)


def do_home(command, parser):
    parser.turtle.home()


def do_pendown(command, parser):
    parser.turtle.pendown()


def do_penup(command, parser):
    parser.turtle.penup()


def do_setpencolor(command, parser):
    p1 = command.args['color']
    parser.turtle.setpencolor(p1)


class Command:
    # Dispatch Table!
    dispatch_table = {
        "forward": do_forward,
        "back": do_back,
        "left": do_left,
        "right": do_right,
        "setpos": do_setpos,
        "setxy": do_setxy,
        "setx": do_setx,
        "sety": do_sety,
        "home": do_home,
        "pendown": do_pendown,
        "penup": do_penup,
        "setpencolor": do_setpencolor,
    }

    def __init__(self, command, args):
        self.name = command
        self.args = args

    def __repr__(self):
        return f"Command({self.name}, {self.args})"

    def line(self, parser):
        self.dispatch_table[self.name](self, parser)
