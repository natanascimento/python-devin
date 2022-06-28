from .entity import Aluno, Media, \
                    Escritor, Caneta, Lapis


def exemplo1():
    aluno = Aluno(nome="natan", dia_nascimento=26,
                  mes_nascimento=4, ano_nascimento=1999,
                  matricula=123, cpf="12312312")

    media = Media(av1=9.8, av2=9.1)

    aluno.nota_final = media.media

    print(aluno.get_info())


def exemplo2():
    escritor = Escritor(nome="Natan")
    caneta = Caneta(marca="SENAI")
    lapis = Lapis(marca="SENAI")

    escritor.ferramenta = lapis
    escritor.ferramenta.escrever()


def main():
    exemplo2()
