from CalculadoraEstatisticas import CalculadoraEstatisticas
from MatrizConfusao import MatrizConfusao
from MatrizAcertos import MatrizAcertos
from LeitorArquivo import LeitorArquivo, LeitorArquivoComTestes
from KNN import KNN

import sys

def main():
    if len(sys.argv) < 4:
        print("Número inválido de argumentos. Abortando")
        print("Passe: \n 1 - Caminho do arquivo \n 2 - Porcentagem para usar de teste \n 3 - Números de K")
        print("Ex: python3 main.py spambase/spambase.data 0.1 1 3 5 7 9 \n")
        sys.exit()
    dados = LeitorArquivoComTestes(sys.argv[1], float(sys.argv[2]))
    knn = KNN(dados[0])
    k_para_teste = sys.argv[3:]
    for index, k in enumerate(k_para_teste):
        k_para_teste[index] = int(k)
    
    for k in k_para_teste:
        print("\n\n************* TESTANDO PARA K = " + str(k) + "**********************\n\n")
        resultado_knn = knn.run(dados[1], k)
        resultados_esperados = []
        for dado in dados[1]:
            resultados_esperados.append(dado[-1])
        
        matrizConfusao = MatrizConfusao(dados[2])
        matrizConfusao.geraMatriz(resultado_knn, resultados_esperados)
        print(matrizConfusao)


        calculadoraEstatisticas = CalculadoraEstatisticas(matrizConfusao)

        print(calculadoraEstatisticas)
        print("\n\n************* TÉRMINO DO TESTE PARA K = " + str(k) + "**********************\n\n")


    

main()