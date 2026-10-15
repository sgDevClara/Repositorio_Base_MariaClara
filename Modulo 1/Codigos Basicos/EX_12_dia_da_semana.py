# Crie um programa que receba um número inteiro e dia qual é o dia da semana correspondente a este número
# Os dias são:
# 1 - domingo
# 2 - Segunda
# 3 - Terça
# 4 - Quarta
# 5 - Quinta
# 6 - Sexta
# 7 - Sábado

# OUTPUT ESPERADO

# Digite um número: 1
# Domingo

# Digite um número: 2
# Segunda

# Digite um número: 8
# Número errado

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

print('/n------------------------------')
print('/n--------Dias da Semana--------')
print('/n------------------------------')


Dias = int(input("Digite um número: "))

domingo = 1
segunda = 2
terça = 3
quarta = 4
quinta = 5
sexta = 6
sábado = 7

if Dias == 1:
    print("Hoje é domingo!")
elif Dias == 2:
    print("Hoje é segunda!")
elif Dias == 3:
    print("Hoje é terça!")
elif Dias == 4:
    print("Hoje é quarta!")
elif Dias == 5:
    print("Hoje é quinta!")
elif Dias == 6:
    print("Hoje é sexta!")
elif Dias == 7:
    print("Hoje é sábado!")
else:
    print("Número errado")
