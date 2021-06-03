from modules import *

valores1 = [2, -2, -2, -1]
valores2 = [2, -2, 2, 1]
objetivos = [0, 1, 0, 1]
pesos = [0, 0, 0]

flag = True
cont = 0
while flag:
    flag = False
    print(f'\nIteração externa: {cont}')
    for i in range(len(valores1)):
        print(f'\nIteração: {i}')

        soma = somaponderada(valores1[i], valores2[i], pesos[0], pesos[1], pesos[2])
        print(f'Soma ponderada: {soma}')

        parametrizacao = limiar(soma)
        print(f'Parametrização: {parametrizacao}')

        erro = calculaerro(objetivos[i], parametrizacao)
        print(f'Erro: {erro}')

        if erro != 0:
            flag = True
            pesos = atualizapesos(valores1[i], valores2[i],
                                    pesos[0], pesos[1], pesos[2], erro)
            
        print(f'Pesos: {pesos}')
    cont+=1

print(f'\nAo final das iterações ocorreram:\n\tIterações:{cont}\n\tPesos: {pesos}')