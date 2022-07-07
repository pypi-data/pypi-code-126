from parser import *
from lexer import *
from tokens import *
class Calcium:
    def __init__(self, equation : str):
        if type(equation) != str:
            raise Exception("The Equation must be a String!")
        self.eq = equation
        self.lexer = lex.lex()
        self.parser = yacc.yacc(debug=False, write_tables=False)
        self.result = self.parser.parse(self.eq)
    def __str__(self):
        return str(self.result)
    def solve(self):
        return self.result