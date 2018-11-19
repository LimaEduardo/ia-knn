def LeitorArquivo(nomeArquivo):
    with open(nomeArquivo) as arquivo:
        linhas = arquivo.read().splitlines()
    dados = []
    for linha in linhas:
        lista = linha.strip().split(',')
        dados.append([])
        for i in range(len(lista) - 1):
            dados[-1].append(float(lista[i]))
        dados[-1].append(lista[-1])
    return dados


LeitorArquivo("spambase/spambase.data")