from CalculadoraEstatisticas import CalculadoraEstatisticas
from MatrizAcertos import MatrizAcertos
from LeitorArquivo import LeitorArquivo
from KNN import KNN

def main():
    # matrizAcertos = MatrizAcertos(10, 2, 3, 9)
    # calculadoraEstatisticas = CalculadoraEstatisticas(matrizAcertos)


    # print(matrizAcertos)
    # print(calculadoraEstatisticas)

    # dados = LeitorArquivo("spambase/spambase.data")
    dados_iris = LeitorArquivo("irisbase/iris.data")
    # print(dados)
    knn = KNN(dados_iris)
    teste_iris = [6.3,3.4,5.6,2.4]
    # teste = [0,0,1.42,0,0.71,0.35,0,0.35,0,0.71,0,0.35,0,0,0,5.35,0,0,3.21,0,2.85,0,0.35,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.102,0,0.357,0,0,1.971,24,205]
    print(knn.run(teste_iris,3))
    

main()