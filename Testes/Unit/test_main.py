from main import somar, dividir, multiplicar


def teste_somar():
    # 1 - Prepara

    numero_a = 8
    numero_b = 7
    resultado_esperado = 15

    # 2 - Executa
    resultado_obtido = somar(8, 7)
    # 3 - Valida
    assert resultado_obtido == resultado_esperado

def teste_dividir():

    numero_a = 27
    numero_b = 3
    result_esperado = 9

    # 2 - Executa

    resultado_obtido = dividir(numero_a, numero_b)

    # 3 - Valida

    assert result_esperado == resultado_obtido

def teste_multiplicar():

    numero_a = 27
    numero_b = 3
    resultado_esperado = 81
# 2 - Executa

    resultado_obtido = multiplicar(numero_a, numero_b)

    # 3 - Valida

    assert resultado_esperado == resultado_obtido

def teste_dividir_positivo():
        numero_a = 27
        numero_b = 3
        result_esperado = 9

        # 2 - Executa

        resultado_obtido = dividir(numero_a, numero_b)

        # 3 - Valida

        assert result_esperado == resultado_obtido

def teste_dividir_negativo():
            numero_a = -27
            numero_b = 0
            result_esperado = 'Não Dividiras por Zero'

            # 2 - Executa

            resultado_obtido = dividir(numero_a, numero_b)

            # 3 - Valida

            assert result_esperado == resultado_obtido



# TDD = teste driven development
   # Desenvolvimento direcionado por Teste
# TDD: Teste é uma medida de progresso

# CI: Continuous Integration
# IC: Integração Continua

# (Build) --> Suite de Testes  --> (Build)
#           Automatizada  Passou
# Ambiente de Desenvolvimento              Então, move >>

# CD: Continuius Delivery
# EC: Entrega Continua

# (Build)  --> Suite -->(Build) produção -- >
#      Dev     de Teste  Muitos

