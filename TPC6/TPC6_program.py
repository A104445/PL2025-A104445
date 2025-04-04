from TPC6_anasin import rec_Parser

#linha = input("Introduza uma expressão aritmética: ")
linha = "2+3"
linha2 = "67-(2+3*4)"
linha3 = "(9-2)*(13-4)"

print("INPUT -> " + linha)
res = rec_Parser(linha)
print("TOTAL -> ", res.eval())

print("-----------------------------------")
print("INPUT -> " + linha2)
res2 = rec_Parser(linha2)
print("TOTAL -> ", res2.eval())

print("-----------------------------------")
print("INPUT -> " + linha3)
res3 = rec_Parser(linha3)
print("TOTAL -> ", res3.eval())