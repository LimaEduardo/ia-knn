from CalculadoraEstatisticas import CalculadoraEstatisticas
from MatrizConfusao import MatrizConfusao
from MatrizAcertos import MatrizAcertos
from LeitorArquivo import LeitorArquivo, LeitorArquivoComTestes
from KNN import KNN

def main():
    matrizAcertos = MatrizAcertos(10, 2, 3, 9)


    # print(matrizAcertos)
    # print(calculadoraEstatisticas)

    # dados = LeitorArquivo("spambase/spambase.data")
    # dados_iris = LeitorArquivo("irisbase/iris.data")
    # print(dados)
    # knn = KNN(dados_iris)
    # teste_iris = [[6.3,3.4,5.6,2.4]]
    # teste = [0,0,1.42,0,0.71,0.35,0,0.35,0,0.71,0,0.35,0,0,0,5.35,0,0,3.21,0,2.85,0,0.35,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.102,0,0.357,0,0,1.971,24,205]
    # print(knn.run(teste_iris,3))

    dados = LeitorArquivoComTestes("spambase/spambase.data", 0.05)
    knn = KNN(dados[0])
    # print(dados[1])
    resultado_knn = knn.run(dados[1], 3)
    resultados_esperados = []
    for dado in dados[1]:
        resultados_esperados.append(dado[-1])
    
    print(resultado_knn)
    print(resultados_esperados)
    matrizConfusao = MatrizConfusao(dados[2])
    matrizConfusao.geraMatriz(resultado_knn, resultados_esperados)

    matConf = matrizConfusao.getMatriz()

    matrizAcertos.negativoNegativo = matConf["0"]["0"]
    matrizAcertos.negativoPositivo = matConf["0"]["1"]
    matrizAcertos.positivoNegativo = matConf["1"]["0"]
    matrizAcertos.positivoPositivo = matConf["1"]["1"]

    print(matrizAcertos)

    calculadoraEstatisticas = CalculadoraEstatisticas(matrizAcertos)

    print(calculadoraEstatisticas)


    

main()