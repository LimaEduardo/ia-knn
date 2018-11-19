from CalculadoraEstatisticas import CalculadoraEstatisticas
from MatrizConfusao import MatrizConfusao
from MatrizAcertos import MatrizAcertos
from LeitorArquivo import LeitorArquivo, LeitorArquivoComTestes
from KNN import KNN

import sys

def main():
    if len(sys.argv) < 3:
        print("Número inválido de argumentos. Abortando")
        print("Passe o caminho do arquivo e a porcentagem para usar de teste")
        sys.exit()
    dados = LeitorArquivoComTestes(sys.argv[1], float(sys.argv[2]))
    knn = KNN(dados[0])
    resultado_knn = knn.run(dados[1], 3)
    resultados_esperados = []
    for dado in dados[1]:
        resultados_esperados.append(dado[-1])
    
    matrizConfusao = MatrizConfusao(dados[2])
    matrizConfusao.geraMatriz(resultado_knn, resultados_esperados)
    print(matrizConfusao)


    calculadoraEstatisticas = CalculadoraEstatisticas(matrizConfusao)

    print(calculadoraEstatisticas)


    

main()