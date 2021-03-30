# Parser.py
import sys
import ply.yacc as yacc
from Lexer import Lexer
from Turtle import Turtle
from Command import Command


class Parser:
    tokens = Lexer.tokens

    def __init__(self):
        self.parser = None
        self.lexer = None
        self.turtle = Turtle()


    def Parse(self, input, **kwargs):
        self.lexer = Lexer()
        self.lexer.Build(input, **kwargs)
        self.parser = yacc.yacc(module=self, **kwargs)
        program = self.parser.parse(lexer=self.lexer.lexer)
        for command in program:
            #print(command)
            command.line(self)

    def p_error(self):
        print("Syntax error", file=sys.stderr)
        exit(1)

    def p_program0(self, p):
        """  program  :   command  """
        p[0] = [p[1]]

    def p_program1(self, p):
        """  program  :  program command  """
        lst = p[1]
        lst.append(p[2])
        p[0] = lst

    def p_command0(self, p):
        """  command  :  fd len """
        args = {'len': p[2]}
        p[0] = Command("forward", args)

    def p_command1(self, p):
        """  command  :  forward len """
        args = {'len': p[2]}
        p[0] = Command("forward", args)

    def p_command2(self, p):
        """  command  :  bk len """
        args = {'len': p[2]}
        p[0] = Command("back", args)

    def p_command3(self, p):
        """  command  :  back len """
        args = {'len': p[2]}
        p[0] = Command("back", args)

    def p_command4(self, p):
        """  command  :  lt deg """
        args = {'deg': p[2]}
        p[0] = Command("left", args)

    def p_command5(self, p):
        """  command  :  left deg """
        args = {'deg': p[2]}
        p[0] = Command("left", args)

    def p_command6(self, p):
        """  command  :  rt deg """
        args = {'deg': p[2]}
        p[0] = Command("right", args)

    def p_command7(self, p):
        """  command  :  right deg """
        args = {'deg': p[2]}
        p[0] = Command("right", args)

    def p_command8(self, p):
        """  command  :  setpos coordinate """
        args = {'coordinate': p[2]}
        p[0] = Command("setpos", args)

    def p_command9(self, p):
        """  command  :  setxy coordinate """
        args = {'coordinate': p[2]}
        p[0] = Command("setxy", args)

    def p_command10(self, p):
        """  command  :  sety y """
        args = {'y': p[2]}
        p[0] = Command("sety", args)

    def p_command11(self, p):
        """  command  :  setx x """
        args = {'x': p[2]}
        p[0] = Command("setx", args)

    def p_command12(self, p):
        """  command  :  home"""
        args = {}
        p[0] = Command("home", args)

    def p_command13(self, p):
        """  command  :  pendown """
        args = {}
        p[0] = Command("pendown", args)

    def p_command14(self, p):
        """  command  :  pd """
        args = {}
        p[0] = Command("pendown", args)

    def p_command15(self, p):
        """  command  :  penup """
        args = {}
        p[0] = Command("penup", args)

    def p_command16(self, p):
        """  command  :  pu  """
        args = {}
        p[0] = Command("penup", args)

    def p_command17(self, p):
        """  command  :  setpencolor color """
        args = {'color': p[2]}
        p[0] = Command("setpencolor", args)

    def p_color(self, p):
        """  color : '[' INT  INT  INT ']' """
        p[0] = (p[2], p[3], p[4])

    def p_len(self, p):
        """  len : INT """
        p[0] = p[1]

    def p_deg(self, p):
        """  deg : INT """
        p[0] = p[1]

    def p_x(self, p):
        """  x : INT """
        p[0] = p[1]

    def p_y(self, p):
        """  y : INT """
        p[0] = p[1]

    def p_coordinate0(self, p):
        """  coordinate : '[' INT  INT ']'
                        | INT  INT  """
        if len(p) == 5:
            p[0] = (p[2], p[3])
        else:
            p[0] = (p[1], p[2])
