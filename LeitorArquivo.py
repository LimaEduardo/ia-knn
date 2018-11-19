import random

def LeitorArquivo(nomeArquivo):
    with open(nomeArquivo) as arquivo:
        linhas = arquivo.read().splitlines()
    dados = []
    conjunto_classes = set()
    for linha in linhas:
        lista = linha.strip().split(',')
        dados.append([])
        for i in range(len(lista) - 1):
            dados[-1].append(float(lista[i]))
        dados[-1].append(lista[-1])
        conjunto_classes.add(lista[-1])
    return [dados, conjunto_classes]

def LeitorArquivoComTestes(nomeArquivo, porcentagem_teste):
    with open(nomeArquivo) as arquivo:
        linhas = arquivo.read().splitlines()
    
    total_linhas = len(linhas)
    conjunto_indices =  {x for x in range(total_linhas)}
    
    total_teste = int(total_linhas * porcentagem_teste)
    total_treino = total_linhas - total_teste

    indices_teste = set(random.sample(range(total_linhas), total_teste))
    indices_treino = conjunto_indices - indices_teste

    dados_teste = []
    dados_treino = []
    conjunto_classes = set()

    for indice in indices_teste:
        lista = linhas[indice].strip().split(',')
        dados_teste.append([])
        for i in range(len(lista) - 1):
            dados_teste[-1].append(float(lista[i]))
        dados_teste[-1].append(lista[-1])
        conjunto_classes.add(lista[-1])
    
    for indice in indices_treino:
        lista = linhas[indice].strip().split(',')
        dados_treino.append([])
        for i in range(len(lista) - 1):
            dados_treino[-1].append(float(lista[i]))
        dados_treino[-1].append(lista[-1])
        conjunto_classes.add(lista[-1])
    
    arquivo_teste = open("arquivo_teste", "w")
    for dado in dados_teste:
        arquivo_teste.write(str(dado)[1:-1] + "\n")
    
    arquivo_treino = open("arquivo_treino", "w")
    for dado in dados_treino:
        arquivo_treino.write(str(dado)[1:-1] + "\n")

    return [dados_treino, dados_teste, conjunto_classes]


LeitorArquivoComTestes("spambase/spambase.data", 0.10)