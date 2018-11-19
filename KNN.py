import math

class KNN:

    def __init__(self, dados):
        self.dados = dados

    def distanciaEuclidiana(self, lista1, lista2):
        resultado = 0
        for i in range(len(lista2) - 1):
            resultado += (lista1[i] - lista2[i])**2
        return math.sqrt(resultado)
    
    def melhoresVizinhos(self, teste, k):
        resultado = []
        for index, dado in enumerate(self.dados):
            resultado.append({'indice' : index, 'distancia' : self.distanciaEuclidiana(teste,dado)})
        resultado_ordenado = sorted(resultado, key=lambda k: k['distancia'])
        # print(resultado)
        return resultado_ordenado[0:k]
    
    def run(self,testes, k):
        resultados = []
        for teste in testes:
            melhores_vizinhos = self.melhoresVizinhos(teste,k)
            
            resultado = {}
            for vizinho in melhores_vizinhos:
                dado = self.dados[vizinho['indice']]
                try:
                    resultado[dado[-1]] += 1
                except KeyError:
                    resultado[dado[-1]] = 1
            
            
            valor_maximo = -1
            chave_maxima = -1
            
            for (chave, valor) in resultado.items():
                if(valor > valor_maximo):
                    valor_maximo = valor
                    chave_maxima = chave
            
            resultados.append(chave_maxima)

        return resultados
    

