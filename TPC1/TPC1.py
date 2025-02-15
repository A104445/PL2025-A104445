def percorreTexto(texto):
    o = False
    of = False
    on = True
    num = ""
    total = 0
    for c in texto:
        if (c.isdigit()) and (on == True):
            num += c
        else:
            if on == True and num != "":
                total += int(num)
            num = ""
            if c.upper() == 'O':
                o = True
            elif (c.upper() == 'F') and (o == True):
                of = True
                o = False
            elif (c.upper() == 'F') and (of == True):
                of = False
                on = False
            elif (c.upper() == 'N') and (o == True):
                o = False
                on = True
            elif c == '=':
                print("Total atual: " + str(total))
    if num != "":
        total += int(num)
    return total

text = input("Escreva um texto: ")
ocorr = percorreTexto(text)
print("Total final: " + str(ocorr))