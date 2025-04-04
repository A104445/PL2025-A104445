import json
import os

nomeFicheiro = "stock.json"
valores = {"2e":2,"1e":1,"50c":0.5,"20c":0.2,"10c":0.1,"5c":0.05}

def lerJson(nomeFicheiro):
    if os.path.exists(nomeFicheiro):
        with open(nomeFicheiro, 'r') as f:
            return json.load(f)
    return []

def salvaJson(nomeFicheiro,produtos):
    with open(nomeFicheiro, 'w') as f:
        json.dump(produtos, f, indent=4)

def calculaSaldo(saldo,moedas):
    lMoedas = moedas.split(", ")
    for moeda in lMoedas:
        if moeda in valores:
            saldo += valores[moeda]
    return saldo

def calculaTroco(troco):
    resto = [0,0,0,0,0,0]
    while troco >= 2:
        resto[0] += 1
        troco -= 2
    while troco >= 1:
        resto[1] += 1
        troco -= 1
    while troco >= 0.5:
        resto[2] += 1
        troco -= 0.5
    while troco >= 0.2:
        resto[3] += 1
        troco -= 0.2
    while troco >= 0.1:
        resto[4] += 1
        troco -= 0.1
    while troco >= 0.05:
        resto[5] += 1
        troco -= 0.05
    return resto

def main():
    print("maq: Stock carregado, Estado atualizado.")
    print("maq: Bom dia. Estou disponível para atender o seu pedido.")
    
    saldo = 0
    produtos = lerJson(nomeFicheiro)
    
    while True:
        comando = input(">> ")
        if comando == "LISTAR":
            print("maq:")
            print("cod | nome | quantidade | preço")
            print("---------------------------------")
            for produto in produtos:
                print(f"{produto['cod']} | {produto['nome']} | {produto['quant']} | {produto['preco']:.2f}")
        if comando.startswith("MOEDA"):
            saldo = calculaSaldo(saldo,comando[6:])
            print(f"maq: Saldo = {saldo}€")
        if comando.startswith("SELECIONAR"):
            cod = comando.split()[1]
            existe = False
            for p in produtos:
                if p['cod'] == cod:
                    existe = True
                    preco = p['preco']
                    if saldo >= preco and p['quant'] > 0:
                        print(f"maq: Pode retirar o produto dispensado \"{p['nome']}\"")
                        saldo -= preco
                        print(f"maq: Saldo = {round(saldo,2)}")
                        p['quant'] -= 1
                    else:
                        if saldo < preco:
                            print(f"maq: Saldo insuficiente para satisfazer o seu pedido")
                            print(f"maq: Saldo = {round(saldo,2)}; Pedido = {preco}")
                        else:
                            print(f"maq: Produto não disponível.")
            if not existe:
                print("maq: Produto não encontrado.")
        if comando == "SAIR":
            salvaJson(nomeFicheiro,produtos)
            troco = calculaTroco(saldo)
            print(f"Troco: {saldo}€")
            if troco[0] > 0:
                print(f"- {troco[0]} moedas de 2€") 
            if troco[1] > 0:
                print(f"- {troco[1]} moedas de 1€")
            if troco[2] > 0:
                print(f"- {troco[2]} moedas de 0.5€")
            if troco[3] > 0:
                print(f"- {troco[3]} moedas de 0.2€")
            if troco[4] > 0:
                print(f"- {troco[4]} moedas de 0.1€") 
            if troco[5] > 0:
                print(f"- {troco[5]} moedas de 0.05€")
            print("maq: Até à próxima")
            break
            
        comando = ""


if __name__ == "__main__":
    main()