class Funcionario:

    def __init__(self, nome: str, funcao: str):
        self.nome = nome
        self.funcao = funcao


class Empresa:

    def __init__(self, nome: str):
        self.nome = nome
        self.funcionarios = []
    
    def cadastrar_funcionario(self, nome, funcao):
        self.funcionarios.append(Funcionario(nome = nome, funcao = funcao))

    def listar_funcionarios(self):
        for funcionario in self.funcionarios:
            print(f"Funcionário: {funcionario.nome}, Função: {funcionario.funcao}, Empresa: {self.nome}")


empresa_1 = Empresa('Conecta')

empresa_1.cadastrar_funcionario('Breno', '0')
empresa_1.cadastrar_funcionario('Maycon', '1')
empresa_1.cadastrar_funcionario('Natan', '2')

empresa_1.listar_funcionarios()
