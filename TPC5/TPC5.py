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
    resto = []
    

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
            print("maq: Até à próxima")
            break
            
        comando = ""


if __name__ == "__main__":
    main()