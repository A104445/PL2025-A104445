import ply.lex as lex

tokens = ('NUM','PA','PF','ADD','MULT','SUB','DIV','FIM')

t_NUM = r'\d+'
t_PA = r'\('
t_PF = r'\)'
t_ADD = r'\+'
t_MULT = r'\*'
t_SUB = r'-'
t_DIV = r'/'
t_FIM = r'\$'


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = '\t '

def t_error(t):
    print('Carácter desconhecido: ', t.value[0])
    t.lexer.skip(1)
    
lexer = lex.lex()
