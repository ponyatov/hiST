import ply.lex as lex

tokens = ['SYM']

def t_error(t): raise SyntaxError(t)

def t_SYM(t):
    r'[a-zA-Z0-9_]+'
    return t

lexer = lex.lex()

def REPL():
    while True:
        lexer.input(raw_input("pyst> "))
        
if __name__ == '__main__': REPL()