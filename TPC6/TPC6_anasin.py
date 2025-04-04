from TPC6_analex import lexer
from TPC6_ast import Exp, Num, BinOp 

prox_simb = ('Erro', '', 0, 0)

def parserError(simb):
    print("Erro sintático, token inesperado: ", simb)

def rec_term(simb):
    global prox_simb
    if prox_simb is None: 
        prox_simb = ('FIM', '', 0, 0)
    if prox_simb.type == simb:
        prox_simb = lexer.token()
    else:
        parserError(prox_simb)
        prox_simb = ('erro', '', 0, 0)
        
# P1: Exp -> Termo Exp2
# P2: Exp2 -> '+' Exp
# P3: Exp2 -> '-' Exp
# P4: Exp2 -> 
# P5: Termo -> Fator Termo2
# P6: Termo2 -> '*' Termo
# P7: Termo2 -> '/' Termo
# P8: Termo2 -> 
# P9: Fator -> '(' Exp ')'
# P10: Fator -> num

def rec_Fator():
    global prox_simb
    if prox_simb.type == 'PA':
        print("Derivando por P9: Fator -> '(' Exp ')'")
        rec_term('PA')
        expr = rec_Exp()
        rec_term('PF')
        print("Reconheci P9: Fator -> '(' Exp ')'")
        return expr
    elif prox_simb.type == 'NUM':
        print("Derivando por P10: Fator -> num")
        valor = prox_simb.value
        rec_term('NUM')
        print("Reconheci P10: Fator -> num")
        return Num(valor)
    else:
        parserError(prox_simb)
    
def rec_Termo2(left):
    global prox_simb
    if prox_simb is None:
        return left
    if prox_simb.type == 'MULT':
        print("Derivando por P6: Termo2 -> '*' Termo")
        rec_term('MULT')
        right = rec_Termo()
        left = BinOp(left, '*', right)
        print("Reconheci P6: Termo2 -> '*' Termo")
        return left
    elif prox_simb.type == 'DIV':
        print("Derivando por P7: Termo2 -> '/' Termo")
        rec_term('DIV')
        right = rec_Termo()
        left = BinOp(left, '/', right)
        print("Reconheci P7: Termo2 -> '/' Termo")
        return left
    elif prox_simb.type == 'ADD':
        print("Derivando por P8: Termo2 ->")
        print("Reconheci P8: Termo2 ->")
    elif prox_simb.type == 'SUB':
        print("Derivando por P8: Termo2 ->")
        print("Reconheci P8: Termo2 ->")
    elif prox_simb.type == 'PF':
        print("Derivando por P8: Termo2 ->")
        print("Reconheci P8: Termo2 ->")
    elif prox_simb.type == 'FIM':
        print("Derivando por P8: Termo2 ->")
        print("Reconheci P8: Termo2 ->")
    else:
        parserError(prox_simb)
    return left
    
def rec_Termo():
    global prox_simb
    print("Derivando por P5: Termo -> Fator Termo2")
    left = rec_Fator()
    left = rec_Termo2(left)
    print("Reconheci P5: Termo -> Fator Termo2")
    return left

def rec_Exp2(left):
    global prox_simb
    if prox_simb is None:
        return left
    if prox_simb.type == 'ADD':
        print("Derivando por P2: Exp2 -> '+' Exp")
        rec_term('ADD')
        right = rec_Exp()
        left = BinOp(left, '+', right)
        print("Reconheci P2: Exp2 -> '+' Exp")
        return left
    elif prox_simb.type == 'SUB':
        print("Derivando por P3: Exp2 -> '-' Exp")
        rec_term('SUB')
        right = rec_Exp()
        left = BinOp(left, '-', right)
        print("Reconheci P3: Exp2 -> '-' Exp")
        return left
    elif prox_simb.type == 'PF':
        print("Derivando por P4: Exp2 ->")
        print("Reconheci P4: Exp2 ->")
    elif prox_simb.type == 'FIM':
        print("Derivando por P4: Exp2 ->")
        print("Reconheci P4: Exp2 ->")
    else:
        parserError(prox_simb)
    return left
    
def rec_Exp():
    global prox_simb
    print("Derivando por P1: Exp -> Termo Exp2")
    left = rec_Termo()
    left = rec_Exp2(left)
    print("Reconheci P1: Exp -> Termo Exp2")
    return left

def rec_Parser(data):
    global prox_simb
    lexer.input(data)
    prox_simb = lexer.token()
    return rec_Exp()
