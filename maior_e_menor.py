# Passo 1: Criar uma lista vazia para armazenar os números
numeros = []

# Passo 2: Usar um laço FOR para pedir 5 números ao usuário
for i in range(5):
    num = float(input(f"Digite o {i+1}º número: "))  # Pede um número e converte para float
    numeros.append(num)  # Adiciona o número na lista

# Passo 3: Ordenar a lista do maior para o menor
numeros.sort(reverse=True)  # Ordena em ordem decrescente

# Passo 4: Exibir a lista ordenada
print("\nNúmeros ordenados do maior para o menor:")
print(numeros)

# Passo 5: Mostrar o maior e o menor número
print(f"O maior número é: {numeros[0]}")
print(f"O menor número é: {numeros[-1]}")