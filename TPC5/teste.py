import json
import os

STOCK_FILE = "stock.json"
COINS = {"1e": 100, "50c": 50, "20c": 20, "10c": 10, "5c": 5, "2c": 2, "1c": 1}

stock = [
    {"cod": "A23", "nome": "água 0.5L", "quant": 8, "preco": 0.7},
    {"cod": "B45", "nome": "coca-cola 0.33L", "quant": 5, "preco": 1.2},
    {"cod": "C12", "nome": "batatas fritas", "quant": 10, "preco": 1.0},
    {"cod": "D34", "nome": "chocolate", "quant": 3, "preco": 1.5}
]

def listar_stock(stock):
    print("cod | nome | quantidade | preço")
    print("-" * 40)
    for item in stock:
        print(f"{item['cod']} | {item['nome']} | {item['quant']} | {item['preco']}€")

def inserir_moeda(saldo, moedas):
    for moeda in moedas.split(","):
        moeda = moeda.strip()
        if moeda in COINS:
            saldo += COINS[moeda]
    return saldo

def selecionar_produto(stock, saldo, codigo):
    for item in stock:
        if item["cod"] == codigo:
            if item["quant"] > 0:
                if saldo >= int(item["preco"] * 100):
                    item["quant"] -= 1
                    saldo -= int(item["preco"] * 100)
                    print(f"Pode retirar o produto dispensado \"{item['nome']}\"")
                else:
                    print(f"Saldo insuficiente para satisfazer o seu pedido")
                    print(f"Saldo = {saldo}c; Pedido = {int(item['preco'] * 100)}c")
            else:
                print("Produto esgotado.")
            return saldo
    print("Produto inexistente.")
    return saldo

def calcular_troco(saldo):
    troco = []
    for moeda, valor in sorted(COINS.items(), key=lambda x: -x[1]):
        while saldo >= valor:
            saldo -= valor
            troco.append(moeda)
    return troco

def adicionar_produto(stock, codigo, nome, quantidade, preco):
    for item in stock:
        if item["cod"] == codigo:
            item["quant"] += quantidade
            print("Quantidade atualizada.")
            return
    stock.append({"cod": codigo, "nome": nome, "quant": quantidade, "preco": preco})
    print("Produto adicionado.")

def main():
    saldo = 0
    print("maq: Stock carregado, Estado atualizado.")
    print("maq: Bom dia. Estou disponível para atender o seu pedido.")
    
    while True:
        comando = input(">> ").strip().upper()
        if comando == "LISTAR":
            listar_stock(stock)
        elif comando.startswith("MOEDA"):
            moedas = comando[6:].strip()
            saldo = inserir_moeda(saldo, moedas)
            print(f"maq: Saldo = {saldo}c")
        elif comando.startswith("SELECIONAR"):
            codigo = comando[10:].strip()
            saldo = selecionar_produto(stock, saldo, codigo)
            print(f"maq: Saldo = {saldo}c")
        elif comando == "SAIR":
            troco = calcular_troco(saldo)
            print(f"maq: Pode retirar o troco: {', '.join(troco)}.")
            print("maq: Até à próxima")
            salvar_stock(stock)
            break
        elif comando.startswith("ADICIONAR"):
            try:
                _, codigo, nome, quantidade, preco = comando.split(",")
                adicionar_produto(stock, codigo.strip(), nome.strip(), int(quantidade.strip()), float(preco.strip()))
            except ValueError:
                print("Comando inválido. Formato correto: ADICIONAR, código, nome, quantidade, preço")
        else:
            print("Comando inválido.")

if __name__ == "__main__":
    main()