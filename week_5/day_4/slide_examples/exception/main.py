if __name__ == "__main__":
    try:
        a = int(input("Informe um valor: "))
        b = int(input("Informe um segundo valor: "))
        nota_final = (a+b)/2
    except Exception as exception:
        print(f"TIVEMOS UM ERRO -> {exception}")
    else:
        print(f"O resultado final foi {nota_final}")
    finally:
        print("O SENAI agradece a visita!")
