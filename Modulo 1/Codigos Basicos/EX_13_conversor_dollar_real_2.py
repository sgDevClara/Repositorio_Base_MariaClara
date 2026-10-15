# Atualize o código do exercício de conversor de dollar para real. Agora um "MENU" de opções aparecerá na tela pedindo ao usuário que escolha se quer converter
# de Reais para Dollar ou Dollar para reais. O usuário deve digitar a opção antes de informar os valores.

# OUTPUT ESPERADO:

#------- Exemplo 1 (Dólares para Reais):

# Escolha uma opção: 
# 1 - Dollar para Real
# 2 - Real para dollar
# Digite a opção: 1
# Informe a cotação atual do Dollar: 5.65
# Informe a quantidade de dólares: 150 
# O valor em reais é R$847.50

#---------- Exemplo 2 (Reais para Dólares)

# Escolha uma opção: 
# 1 - Dollar para Real
# 2 - Real para dollar
# Digite a opção: 2
# Informe a cotação atual do Dollar: 5.65
# Informe a quantidade de reais: 150
# O valor em dólares é $26.55

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

print('/n-----------------------------------------/n')
print('/n--------------BEM VINDO(A)---------------/n')
print('/n-----------------------------------------/n')


print('/n----------------Conversor----------------/n')

print("1 - Dólar para real")
print("2 - Real para Dólar")

opções = int(input("Digite uma das opções: "))
if opções == "1":
    cotacao = float(input("Digite a cotação atual do dolar: "))
    dollar_real = float(input("Digite o valor em dólar a ser convertido para real: "))
    real = cotacao * dollar_real
    print("Seu valor em R$ é: ", real)
elif opções == "2":
    real = float(input("Digite a cotação atual do dólar: "))
    cotacao = float(input("Digite a quanidade de reais: "))
    dolar = real / cotacao
    print(f"Seu valor em U$ é de {dolar} e ${real:.2f}")
else:
    print("Digite uma opção válida.")
