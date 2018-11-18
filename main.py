from CalculadoraEstatisticas import CalculadoraEstatisticas
from MatrizAcertos import MatrizAcertos

def main():
    matrizAcertos = MatrizAcertos(10, 2, 3, 9)
    calculadoraEstatisticas = CalculadoraEstatisticas(matrizAcertos)


    print(matrizAcertos)
    print(calculadoraEstatisticas)
    

main()