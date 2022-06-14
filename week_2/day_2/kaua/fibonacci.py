# A Série de FIBONACCI é definida como tendo os dois primeiros termos iguais a 1 e cada termo seguinte (a partir do terceiro) igual à soma dos dois termos imediatamente anteriores. 

# Elaborar um algoritmo que imprima os 15 primeiros termos da Série de Fibonacci.


enesimo_termo = int(input('Qual a quantidade de termos você quer? '))
ultimo_termo = 1
penultimo_termo = 1
i = 3

while i <= enesimo_termo:
    a15 = ultimo_termo + penultimo_termo
    penultimo_termo = ultimo_termo
    ultimo_termo = a15
    i += 1

print(a15)