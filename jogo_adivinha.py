import random
numero_secreto = random.randint(1, 10)
tentativas = 0
limite_tentativas = 5
print("Bem-vindo ao jogo de adivinhação!")
print("Você tem 3 tentativas para adivinhar o número secreto entre 1 e 10.")
while tentativas < limite_tentativas:
    palpite = int(input("Digite seu palpite: "))
    tentativas += 1
    if palpite < numero_secreto:
        print("Muito baixo! Tente novamente.")
    elif palpite > numero_secreto:
        print("Muito alto! Tente novamente.")
    else:
        print(f"Parabéns! Você adivinhou o número secreto {numero_secreto} em {tentativas} tentativas!")
        