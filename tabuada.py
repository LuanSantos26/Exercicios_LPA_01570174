print("---Olá Bem vindo ao meu programa---")
print("1 - Tabuada")
input_usuario = int(input("Digite um número para ver a tabuada: "))
print(f"Tabuada do {input_usuario}:")
for i in range(1, 11):
    resultado = input_usuario * i
    print(f"{input_usuario} x {i} = {resultado}")