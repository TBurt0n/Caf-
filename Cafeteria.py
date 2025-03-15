from datetime import datetime

cafes = {
    "expresso": {"pequeno": 5.00, "médio": 7.00, "grande": 8.50},
    "capuccino": {"pequeno": 6.00, "médio": 8.00, "grande": 10.00},
    "latte": {"pequeno": 7.00, "médio": 9.00, "grande": 11.50}

}

while True:
    cafe_escolhido = input("Selecione o café! (expresso, capuccino, latte): ").lower()
    tamanho = input("Escolha o tamanho (pequeno, médio, grande): ").lower()
    preco = cafes[cafe_escolhido][tamanho]


    hoje = datetime.today().weekday()  # Segunda-feira é 0
    if hoje == 0:
            desconto = preco * 0.10
            preco -= desconto
            print(f"Hoje é segunda! Desconto de 10% aplicado.")
        

    if cafe_escolhido not in cafes or tamanho not in cafes[cafe_escolhido]:
        print("Opção inválida! Tente novamente.")
    else:
        print(f"O preço do seu {cafe_escolhido} {tamanho} é R$ {preco:.2f}.")

    continuar = input ("Deseja continuar com outro pedido? (sim/nao) ").lower()
    if continuar == "nao":
         print("Obrigado pela compra! Até logo!")
         break 

