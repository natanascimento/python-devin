class Cliente:

    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.enderecos = []
        self.class_name = __class__.__name__

    def cadastrar_endereco(self, cidade: str, estado: str):
        self.enderecos.append(Endereco(cidade=cidade,
                                       estado=estado))

    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(f"O Cliente {self.nome} reside em {endereco.cidade}-{endereco.estado}")

    def __del__(self):
        print(f"REMOVENDO {self.nome} e {self.enderecos}")


class Endereco:

    def __init__(self, cidade: str, estado: str):
        self.cidade = cidade
        self.estado = estado

    def __del__(self):
        print(f"REMOVENDO CLASSE ENDERECO COM {self.cidade} e {self.estado}")


if __name__ == "__main__":
    cliente = Cliente(nome="Natan")

    #cliente.cadastrar_endereco(cidade="Aracaju",
                               #estado="SE")
    cliente.listar_enderecos()

    print("NOME DA MINHA CLASSE", cliente.class_name)

    del cliente