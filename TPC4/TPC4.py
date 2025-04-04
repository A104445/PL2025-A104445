import re
import ply.lex as lex

texto = """
select ?nome ?desc where {
?s dbo:MusicalArtist.
?s foaf:name "Chuck Berry"@en .
?w dbo:artist ?s.
?w foaf:name ?nome.
?w dbo:abstract ?desc
} LIMIT 1000
"""

tokens = (
    'SELECT', 
    'WHERE', 
    'LIMIT', 
    'VAR', 
    'DBO', 
    'FOAF', 
    'ACHA',
    'FCHA', 
    'PONTO', 
    'STRING_LITERAL',
    'IDIOMA', 
    'NUM',
    'A' 
)

t_ACHA = r'\{'
t_FCHA = r'\}'
t_PONTO = r'\.'
t_A = r'a'

def t_SELECT(t):
    r'select'
    return t

def t_WHERE(t):
    r'where'
    return t

def t_LIMIT(t):
    r'LIMIT'
    return t


def t_VAR(t):
    r'[?][a-zA-Z][a-zA-Z0-9_]*'
    return t

def t_DBO(t):
    r'dbo:[a-zA-Z]+'
    return t


def t_FOAF(t):
    r'foaf:[a-zA-Z]+'
    return t

def t_NUM(t):
    r'[0-9]+'
    return t

def t_STRING_LITERAL(t):
    r'"(.+)"'
    return t

def t_IDIOMA(t):
    r'@(.+)'
    return t

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Erro léxico: caracter ilegal '{t.value[0]}'")
    t.skip(1)
    

lexer = lex.lex()

lexer.input(texto)

print("INPUT")
print(texto)
print("-------------------------------------------------")
print("OUTPUT")

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)