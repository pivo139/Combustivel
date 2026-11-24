
resp = "s"

while resp == "s":
     
    alcool = float(input("Digite o valor do alcool: "))

    gasolina = float(input("Digite o valor da gasolina: "))


    combustivel = alcool / gasolina

    if combustivel <= 0.70:
        print("Vale a pena colocar alcool")

    if combustivel >= 0.70:
        print("Vale a pena colocar gasolina")


    resp = input(("Deseja refazer a aplicação? (s/n)"))

    if resp == "s":
        print("Vamos lá então!")

    
print("Obrigado, volte sempre!")