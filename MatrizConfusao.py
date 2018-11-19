from prettytable import PrettyTable

class MatrizConfusao:
    def __init__(self, conjunto_classes):
        self.classes = conjunto_classes
        self.matriz = {}
        for classe in self.classes:
            self.matriz[classe] = {}
            for sub_classe in self.classes:
                self.matriz[classe][sub_classe] = 0

    
    def geraMatriz(self, resultados_obtidos, resultados_esperados):
        for i in range(len(resultados_esperados)):
            self.matriz[resultados_esperados[i]][resultados_obtidos[i]] += 1
        

    def getMatriz(self):
        return self.matriz 

    def getClasses(self):
        return list(self.classes)

    def __str__(self):
        saida = PrettyTable()
        campos = [""]
        for classe in self.classes:
            campos.append(classe)
        saida.field_names = campos

        itens = campos[1:]
        for classe in itens:
            linha = [classe]
            for sub_classe in itens:
                linha.append(self.matriz[classe][sub_classe])
            saida.add_row(linha)
        
        return saida.__str__()

    