def stringer(func):
    
    def inverter(str):
        # inverte a string
        return str[::-1]
    
    return inverter

# usando decorators
@stringer
def funcao_chama(str):
    return str

teste_1 = funcao_chama("Breno")
print(teste_1)
