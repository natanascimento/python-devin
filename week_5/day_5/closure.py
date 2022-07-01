def validar(f):

    def valida():
        print("VALIDEI")

    return valida


if __name__ == "__main__":
    validar("f")()
