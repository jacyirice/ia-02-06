def calculaerro(v1, v2):
    return v1 - v2


def somaponderada(valor1, valor2, peso1, peso2, bias):
    return valor1 * peso1 + valor2 * peso2 + bias


def limiar(v):
    if v >= 0:
        return 1
    return 0


def atualizapesos(valor1, valor2, peso1, peso2, bias, erro):
    peso1 = peso1 + erro * valor1
    peso2 = peso2 + erro * valor2
    bias = bias + erro
    return [peso1, peso2, bias]


if __name__ == '__main__':
    print(calculaerro(2, 1) == 1)
    print(somaponderada(2, 3, 1, 2, 4) == 12)
    print(limiar(1) == 1)
    print(atualizapesos(1, 3, 1, 2, 4, 2) == [3, 8, 6])
