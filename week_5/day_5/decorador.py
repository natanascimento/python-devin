class SomaException(Exception):

    def __init__(self, message):
        super().__init__(message)


def validador(f):

    def valida(x, y):
        if x is None or y is None:
            raise SomaException("Valores nulos não são aceitos nesse calculo")
        if not isinstance(x, int) or not isinstance(y, int):
            raise SomaException("Para realizar o calculo da soma é necessário"
                                " que o numeros sejam inteiros")

        return f(x, y)

    return valida


@validador
def soma(x, y):
    return x + y


@validador
def media(x, y):
    return soma(x, y) / 2


if __name__ == "__main__":
    print(media(3, 3))
