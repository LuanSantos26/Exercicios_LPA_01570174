
numero1=input("Digite o primeiro número: ")
numero2=input("Digite o segundo número: ")
print(" Escolha a operação desejada ""1=soma", "2=subtração", "3=multiplicação", "4=divisão")
escolha = int(input("Digite o número da operação desejada: "))
try:
    if escolha == 1:
        resultado = float(numero1) + float(numero2)
        print(f"O resultado da soma é: {resultado}")
    elif escolha == 2:
        resultado = float(numero1) - float(numero2)
        print(f"O resultado da subtração é: {resultado}")
    elif escolha == 3:
        resultado = float(numero1) * float(numero2)
        print(f"O resultado da multiplicação é: {resultado}")
    elif escolha == 4:
        if float(numero2) != 0:
            resultado = float(numero1) / float(numero2)
            print(f"O resultado da divisão é: {resultado}")
        else:
            print("Erro: Divisão por zero não é permitida.")
    else:
        print("Operação inválida. Por favor, escolha uma operação válida.")
except ValueError:
     print("Erro: Por favor, insira números válidos.")