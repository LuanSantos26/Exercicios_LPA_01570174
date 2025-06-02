nome = input("Digite seu nome: ")
idade= input("Digite sua idade: ")
try:
    idade = int(idade)  # Tenta converter a idade para um número inteiro
    while idade <=18 or idade >= 60:
        print("Idade inválida. Por favor, digite uma idade entre 19 e 59.")
        idade = int(input("Digite sua idade: "))
    print(f"Olá {nome}, sua idade é {idade}.")
except ValueError:
    print("Por favor, digite um número válido para a idade.")
# Passo 1: Criar uma lista vazia para armazenar os números