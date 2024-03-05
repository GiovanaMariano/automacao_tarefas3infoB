"""
Criar um programa que recebe 2 numeros reais como entrada e um operador
matematico. de acordo com o operador matemático fornecido. O programa 
deve calcular e arpesentar o resultado da operação.
EX de entrada...
1.2
2.3
+

EX de Saida...
o resultado da soma é 3.5
"""

print('Digite dois números: ')
número1 = int(input())
número2 = int(input())
print('Digite 1 para soma(+), 2 para subtração(-), 3 para divisão(/), 4 para multiplicação(*): ')
operador = int(input())

if (operador == 1):
       númeroS = número1 + número2
       print("A soma é:", númeroS)
if (operador == 2):
       númeroS = número1 - número2
       print("A subtração é:", númeroS)
if (operador == 3):
       númeroS = número1 / número2
       print("A divisão é:", númeroS)
if (operador == 4):
       númeroS = número1 * número2
       print("A multiplicação é:", númeroS)
