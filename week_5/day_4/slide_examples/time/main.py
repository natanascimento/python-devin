import time


def retorna_hora():
    print(time.asctime(time.localtime()))
    time.sleep(1)
    print(time.strftime("%d/%b/%Y", time.localtime()))


if __name__ == "__main__":
    hora_inicial = time.time()
    time.sleep(3)
    retorna_hora()
    hora_final = time.time()
    total = hora_final - hora_inicial
    print(f"O tempo de execução da minha função foi de {total}")
