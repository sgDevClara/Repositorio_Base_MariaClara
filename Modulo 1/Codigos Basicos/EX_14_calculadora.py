# Escreva um código que mostre na tela um "MENU" de opções de operações matematicas (Adição, Subtração, Divisão e Multiplicação)
# O usuário deve escolher uma das opções e depois inserir dois números para serem calculados de acordo com a operação escolhida.
# No fim mostre o resultado da operação

# OUTPUT ESPERADO:

#----------------------------------------- Exemplo 1 (Soma)

# |------------------------------|
# | Calculadora
# |------------------------------|
# | 1 - Soma
# | 2 - Subtração
# | 3 - Multiplicação
# | 4 - Divisão 
# |------------------------------|
# | Escolha uma das opções: 1
# | Digite o primeiro número:10
# | Digite o segundo número:10
# | O resultado é: 20.0

# ----------------------------------------- Exemplo 2 (Multiplicação)

# |------------------------------|
# | Calculadora
# |------------------------------|
# | 1 - Soma
# | 2 - Subtração
# | 3 - Multiplicação
# | 4 - Divisão 
# |------------------------------|
# | Escolha uma das opções: 3
# | Digite o primeiro número:10
# | Digite o segundo número:10
# | O resultado é: 100.0

# ----------------------------------------- Exemplo 3 (Opção inválida)

# |------------------------------|
# | Calculadora
# |------------------------------|
# | 1 - Soma
# | 2 - Subtração
# | 3 - Multiplicação
# | 4 - Divisão 
# |------------------------------|
# | Escolha uma das opções: 6
# | Digite o primeiro número:1
# | Digite o segundo número:2
# | ERRO. Escolha uma opção válida.



# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

print('/n-----------------------------------------/n')
print('/n--------------BEM VINDO(A)---------------/n')
print('/n-----------------------------------------/n')


print('/n--------------Calculadora----------------/n')

print("""
1 - Soma
2 - Multiplicação
3 - Subtração
4 - Divisão
""")

opções = int(input("Escolha uma das opções: "))


if opções == 1:
    A = int(input("Digite o primeiro número: "))
    B = int(input("Digite o segundo número: "))
    Soma = A + B
    print("o resultado é: ", Soma)
elif opções == 2:
    A = int(input("Digite o primeiro número: "))
    B = int(input("Digite o segundo número: "))
    Multiplicação = A * B
    print("O resultado é: ", Multiplicação)
elif opções == 3:
    A = int(input("Digite o primeiro número: "))
    B = int(input("Digite o segundo número: "))
    Subtração = A - B
    print("O resultado é: ", Subtração)
elif opções == 4:
    A = int(input("Digite o primeiro número: "))
    B = int(input("Digite o segundo número: "))
    if B != 0:
        Divisão = A / B
        print("O resultado é:", Divisão)
    else:
        print("Não é possível dividir por zero.")
else:
    print("Digite uma opção válida!")
