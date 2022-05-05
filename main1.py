import pytest

def print_oi(name):
    print(f'Hi, {name}')

def somar(numero_a,numero_b):
    return numero_a + numero_b


def dividir(numero_a, numero_b):
    return numero_a / numero_b



if __name__ == '__main__':
    print_oi('Henrique')

    resultado = somar(2, 3)
    print(f'A soma: {resultado}')

def teste_somar():
    # 1 - Prepara

    numero_a=8
    numero_b=7
    resultado_esperado = 15

    # 2 - Executa
    resultado_obtido = somar(8, 7)
    # 3 - Valida
    assert resultado_esperado == resultado_obtido

   def teste_dividir():

       numero_a = 27
       numero_b = 3
       result_esperado = 9

    # 2 - Executa

        resultado_obtido = dividir(3, 27)

    # 3 - Valida

      assert resultado_obtido == result_esperado
