def calcula_erro(v1, v2):
    return v1 - v2

def soma_ponderada(valores, pesos, bias):
    soma = 0
    for i in range(len(valores)):
        soma += valores[i] * pesos[i]
    return soma + bias

def limiar(v, t=0):
    if v > t:
        return 1
    return 0

def atualiza_pesos(valores, pesos, bias, erro):
    novos_pesos = []
    for i in range(len(valores)):
        novos_pesos.append(pesos[i] + erro * valores[i])
        
    novo_bias = bias + erro
    return novos_pesos, novo_bias