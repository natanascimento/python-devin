var_1 = str(input("Insira um texto: "))
var_2 = str(input("Insira um texto: "))
var_3 = str(input("Insira um texto: "))

print("======== TAMANHO DOS TEXTOS ========")
print(len(var_1))
print(len(var_2))
print(len(var_3))

print("======== PRIMEIRO TEXTO QUATRO VEZES ========")
print(var_1 * 4)

print("======== SEGUNDO TEXTO DUAS VEZES ========")
print(var_2 * 2)

print("======== SEGUNDO TEXTO DUAS VEZES ========")
print(var_2 * 3)

print("======== JUNÇÃO DO PRIMEIRO COM O TERCEIRO ========")
var_4 = var_1 + var_3
print(var_4)

print("======== VALIDAÇÃO SE EXISTE O TEXTO 1 NO TEXTO 4 ========") 
print(var_1 in var_4)

print("======== VALIDAÇÃO SE EXISTE O TEXTO 2 NO TEXTO 4 ========")
print(var_2 in var_4)

print("======== PRIMEIRO CHAR DO QUARTO TEXTO ========")
print(var_4[0])

print("======== TERCEIRO CHAR DO TERCEIRO TEXTO ========")
print(var_3[2])