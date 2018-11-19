from CalculadoraEstatisticas import CalculadoraEstatisticas
from MatrizConfusao import MatrizConfusao
from MatrizAcertos import MatrizAcertos
from LeitorArquivo import LeitorArquivo, LeitorArquivoComTestes
from KNN import KNN
from prettytable import PrettyTable
def main():
    matrizAcertos = MatrizAcertos(10, 2, 3, 9)


    dados = LeitorArquivoComTestes("spambase/spambase.data", 0.01)
    todasEstatisticas = {}
    print("------------------------------------------")
    for k in [1,3,5,7]:
        knn = KNN(dados[0])
        resultado_knn = knn.run(dados[1], k)
        resultados_esperados = []
        for dado in dados[1]:
            resultados_esperados.append(dado[-1])
        
        print("Resultados obtidos:")
        print(resultado_knn)
        print("Resultados esperados:")
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

        todasEstatisticas[k] = calculadoraEstatisticas
        print("------------------------------------------")
        
    escreveTabelaTodasEstatisticas(todasEstatisticas)

def escreveTabelaTodasEstatisticas(todasEstatisticas):
    saida = PrettyTable()
    header = ["", "Acuracia", "Recall", "Precisao", "F-Score"]
    
    saida.field_names = header
    for k in todasEstatisticas:
        saida.add_row([str(k), todasEstatisticas[k].accuracy, todasEstatisticas[k].truePositiveRate,
                        todasEstatisticas[k].precisao, todasEstatisticas[k].fScore])

    print(saida)


    

main()