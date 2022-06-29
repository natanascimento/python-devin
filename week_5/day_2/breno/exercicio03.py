class Funcionario:

    def __init__(self, funcao: str):
        self.funcao = funcao
        self.funcionarios = []
    
    def cadastrar_funcionario(self, nome):
        self.funcionarios.append(Empresa(nome = nome))

    def listar_funcionarios(self):
        for funcionario in self.funcionarios:
            print(f"Funcionário: {funcionario.nome}, Função: {self.funcao}")


class Empresa:

    def __init__(self, nome: str):
        self.nome = nome

func_1 = Funcionario('Dev')
func_1.cadastrar_funcionario('Breno')
func_1.listar_funcionarios()
