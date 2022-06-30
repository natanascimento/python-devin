from abc import ABC, abstractmethod


class Pagamento(ABC):

    @abstractmethod
    def pagar(self):
        pass

    def validar(self):
        print("VALIDANDO PAGAMENTO")


class PagamentoCartao(Pagamento):

    def pagar(self):
        print("Pagando com Cartao ...")


class ValidadorCartao(PagamentoCartao):

    def pagar(self):
        pass


class PagamentoPix(Pagamento):

    def pagar(self):
        print("Pagando com PIX ...")


if __name__ == "__main__":
    ValidadorCartao().validar()
    ValidadorCartao().pagar()
