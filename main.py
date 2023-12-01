from modules import atualiza_pesos, calcula_erro, soma_ponderada, limiar

entradas = [
    {"valor": [1, 0, 0, 0], "nome": "Onça"},
    {"valor": [1, 0, 0, 1], "nome": "Macaco"},
    {"valor": [1, 0, 1, 0], "nome": "Jacaré"},
    {"valor": [1, 0, 1, 1], "nome": "Lagarto"},
    {"valor": [1, 1, 0, 0], "nome": "Avestruz"},
    {"valor": [1, 1, 0, 1], "nome": "Pato"},
    {"valor": [1, 1, 1, 0], "nome": "Sapo"},
    {"valor": [1, 1, 1, 1], "nome": "Rã"},
]

classes = {
    "00": "Mamífero",
    "01": "Réptil",
    "10": "Ave",
    "11": "Anfíbio",
}

objetivos = [
    [0,0],
    [0,0],
    [0,1],
    [0,1],
    [1,0],
    [1,0],
    [1,1],
    [1,1],
]

num_entradas = len(entradas[0]['valor'])
num_neuronios = len(objetivos[0])

pesos_neuronios = [[0 for _ in range(num_entradas)] for _ in range(num_neuronios)]
bias_neuronios = [0 for _ in range(num_neuronios)]

flag = True
cont = 0
limite_iteracoes = 10

while flag and cont < limite_iteracoes:
    flag = False
    print(f'Iteração externa: {cont}')

    for i in range(len(entradas)):
        nome_animal = entradas[i]['nome']
        valores = entradas[i]['valor']

        erros = []
        somas = []
        parametrizacoes = []

        for n in range(num_neuronios):
            soma = soma_ponderada(valores, pesos_neuronios[n], bias_neuronios[n])
            somas.append(soma)

            param = limiar(soma)
            parametrizacoes.append(param)

            erro = calcula_erro(objetivos[i][n], param)
            erros.append(erro)

            if erro != 0:
                flag = True
                pesos_neuronios[n], bias_neuronios[n] = atualiza_pesos(valores, pesos_neuronios[n], bias_neuronios[n], erro)

        print(f'\nPesos: {pesos_neuronios}, Bias: {bias_neuronios}, Erro: {erros}')
        print(f'Animal: {nome_animal}, Resultado: {parametrizacoes == objetivos[i]}, Classe: {parametrizacoes}')
        
    cont += 1

print(f'\nAo final das iterações ocorreram:\n\tIterações:{cont}\n\tPesos: {pesos_neuronios}\n\tBiases: {bias_neuronios}')
