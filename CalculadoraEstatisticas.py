# Calcula as estatísticas com base em uma matriz de confusão

class CalculadoraEstatisticas:
    def __init__(self, matrizAcertos):
        self.negativoNegativo = matrizAcertos.negativoNegativo
        self.negativoPositivo = matrizAcertos.negativoPositivo
        self.positivoNegativo = matrizAcertos.positivoNegativo
        self.positivoPositivo = matrizAcertos.positivoPositivo

        total = self.negativoNegativo + self.negativoPositivo + self.positivoNegativo + self.positivoPositivo

        # Accuracy: Fracao total correta
        self.accuracy = (self.negativoNegativo + self.positivoPositivo) / (total)
        
        # Recall: numero de predicoes positivas que eram realmente positivas
        self.truePositiveRate = self.positivoPositivo / (self.positivoNegativo + self.positivoPositivo)
        
        self.falsePositiveRate = self.negativoPositivo / (self.negativoNegativo + self.negativoPositivo)
        self.trueNegativeRate = self.negativoNegativo / (self.negativoNegativo + self.negativoPositivo)
        self.falseNegativeRate = self.positivoNegativo / (self.positivoNegativo + self.positivoPositivo)

        # Precisao: numero de acertos positivos em relacao a quantidade real de positivos
        self.precisao = self.positivoPositivo / (self.negativoPositivo + self.positivoPositivo)

        # F-Score: Media harmonica entre precisao e recall
        self.fScore = 2 * (self.truePositiveRate  * self.precisao) / (self.truePositiveRate + self.precisao)


    def __str__(self):
        saida = ""
        saida += "Taxa de falso negativo: " + str(self.falseNegativeRate) + "\n"
        saida += "Taxa de falso positivo: " + str(self.falsePositiveRate) + "\n"
        saida += "Taxa de verdadeiro negativo: " + str(self.trueNegativeRate) + "\n"
        saida += "Taxa de verdadeiro positivo (Recall): " + str(self.truePositiveRate) + "\n"
        saida += "Acuracia: " + str(self.accuracy) + "\n"
        saida += "Precisao: " + str(self.precisao) + "\n"
        saida += "F-Score:  " + str(self.fScore) + "\n"
        return saida