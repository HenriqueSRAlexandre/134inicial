import pytest

def print_oi(name):
    print(f'Hi, {name}')

def somar(numero_a,numero_b):
    return numero_a + numero_b

def dividir(numero_a, numero_b):
    try:
            return numero_a / numero_b
    except ZeroDivisionError:
            return 'Não Dividiras por Zero'

def multiplicar(numero_a, numero_b):
    return numero_a * numero_b



if __name__ == '__main__':
    print_oi('Henrique')

    resultado = somar(2, 3)
    print(f'A soma: {resultado}')

