from functools import reduce


def soma(a: int, b: int) -> int:
    return a + b


soma_lambda = lambda letra: len(letra)

lista_pares = [x for x in range(10)]

x = list(map(lambda valor: valor+10, lista_pares))

y = [x+10 for x in range(10)]

z = list(filter(lambda valor: valor > 15, x))

letras = ["a", "b", "c", "d"]

soma_reduce = reduce(lambda a, b: a+b, letras)

if __name__ == "__main__":
    print(x)
    print(y)
    print(z)
    print(soma_reduce)
