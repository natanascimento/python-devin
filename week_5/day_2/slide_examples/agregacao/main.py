class Aluno:

    def __init__(self, nome: str, matricula: int):
        self.nome = nome
        self.matricula = matricula


class Curso:

    def __init__(self, nome: str):
        self.nome = nome
        self.alunos = []

    def cadastrar_aluno(self, aluno: Aluno):
        self.alunos.append(aluno)

    def listar_alunos(self):
        for aluno in self.alunos:
            print(f"O Aluno {aluno.nome}, cuja matricula {aluno.matricula} encontra-se em nossa base de dados.")


if __name__ == "__main__":
    curso = Curso(nome="Ciências da Computação")

    aluno_1 = Aluno(nome="Natan", matricula=1)
    aluno_2 = Aluno(nome="Maycon", matricula=2)
    aluno_3 = Aluno(nome="Julia", matricula=3)

    curso.cadastrar_aluno(aluno_1)
    curso.cadastrar_aluno(aluno_2)
    curso.cadastrar_aluno(aluno_3)

    curso.listar_alunos()
