# Escreva um programa que pede ao usuário o nome de um aluno e as notas de 3 provas que este aluno realizou.
# No fim o programa deve mostrar na tela a média das 3 provas
# Dica:
# Para calcular a média das provas você deve dividir a soma das notas das provas pela quantidade de provas realizadas
# media = soma / 3

# OUTPUT ESPERADO:

# | ______________________________ |
# | SISTEMA DE PROVAS
# | ______________________________ |
# | Nome do aluno: Fulano
# | Nota da primeira prova: 9.8
# | Nota da segunda prova: 7
# | Nota da terceira prova: 8.5
# | ______________________________ |
# | Aluno: Fulano 
# | Média: 8.43
# | Aluno aprovado
# | ______________________________ |

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------
from colorama import Fore, Style
print('/n------------------------------------/n')
print('/n--------Sistema de Provas-----------/n')
print('/n------------------------------------/n')


aluno = input("Nome do aluno: ")
A = float(input("Nota da primeira prova: "))
B = float(input("Nota da segunda prova: "))
C = float(input("nota da terceira prova: "))

soma = A + B + C
media = soma / 3

print(f"Sua média é: {media:.2f}")
if media >=6:
    print(Fore.GREEN+"Aprovado(a)!", Style.RESET_ALL)
else:
    print(Fore.RED+"Reprovado(a)!", Style.RESET_ALL)
