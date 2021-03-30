# Lexer.py
import ply.lex as lex
import sys


class Lexer:
    literals = "[]"
    t_ignore = " \n\t"
    tokens = ("INT", "VAR", "fd", "forward", "bk", "back", "lt", "left", "rt", "right",
              "setpos", "setxy", "setx", "sety", "setpencolor", "home", "pendown", "penup",
              "pd", "pu")

    def t_COMMAND(self, t):
        r"fd|forward|bk|back|lt|left|rt|right|set(pos)?(xy)?(x)?(y)?(pencolor)?|home|pen(down)?(up)?|pd|pu"
        t.type = t.value
        return t

    def t_INT(self, t):
        r"[0-9]+"
        t.value = int(t.value)
        return t

    def t_VAR(self, t):
        r"""("|:)[a-z][0-9a-z]*"""
        return t

    def t_error(self, t):
        print(f"Parser error. Unexpected char: {t.value}", file=sys.stderr)
        exit(1)

    def __init__(self):
       self.lexer = None

    def Build(self, input, **kwargs):
       self.lexer = lex.lex(module=self, **kwargs)
       self.lexer.input(input)