num_n = int(input("Digite a quantidade de termos: "))

termo_1 = 0
termo_2 = 1
termo_3 = 0

for _ in range(num_n):
    print(termo_3, end=" ")

    termo_3 = termo_1 + termo_2
    termo_2 = termo_1
    termo_1 = termo_3
