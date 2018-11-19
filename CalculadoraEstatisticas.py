# Calcula as estatísticas com base em uma matriz de confusão

class CalculadoraEstatisticas:
    def __init__(self, matrizConfusao):
        self.classes = matrizConfusao.getClasses()
        self.matriz = matrizConfusao.getMatriz()

        self.classesRatings = []

        for classe in self.classes:
            truePositive = self.calculateTruePositive(classe)
            falseNegative = self.calculateFalseNegative(classe)
            falsePositive = self.calculateFalsePositive(classe)
            trueNegative = self.calculateTrueNegative(classe)

            # Recall: numero de predicoes positivas que eram realmente positivas
            try:
                truePositiveRate = truePositive / (truePositive + falseNegative)
            except ZeroDivisionError:
                truePositiveRate = 0

            try:
                # Specificity: numero de predicoes negativas que eram realmente negativas
                trueNegativeRate = trueNegative / (trueNegative + falsePositive)
            except ZeroDivisionError:
                trueNegativeRate = 0

            total = truePositive + falseNegative + falsePositive + trueNegative
            
            # Accuracy: Fracao total correta
            if trueNegative + truePositive != 0:
                accuracy = (trueNegative + truePositive)/total
            else:
                accuracy = "N/A"


            try:
                # Precisao: numero de acertos positivos em relacao a quantidade real de positivos   
                precision = truePositive / (truePositive + falsePositive)
            except ZeroDivisionError:
                precision = "N/A"
            
            fScore = "N/A"
            try:
                # F-Score: Media harmonica entre precisao e recall
                if precision != "N/A":
                    fScore = 2 * (truePositiveRate  * precision) / (truePositiveRate + precision)
            except ZeroDivisionError:
                fScore = "N/A"
            
            classRating = {'nome': classe, 'truePositive': truePositiveRate, 'trueNegative': trueNegativeRate, 'accuracy': accuracy, 'precision': precision, 'fScore': fScore}
            self.classesRatings.append(classRating)
    
    # Taxa de acerto
    def calculateTruePositive(self,classe):
        return self.matriz[classe][classe]
    
    # Soma de todos os números na linha correspondente (exceto a própria classe)
    def calculateFalseNegative(self, classe):
        falseNegative = 0
        for column in self.matriz:
            if column != classe:
                falseNegative += self.matriz[classe][column]
        return falseNegative
    
    # Soma de todos os números na coluna correspondente (exceto a própria classe)
    def calculateFalsePositive(self, classe):
        falsePositive = 0
        for row in self.matriz:
            if row != classe:
                falsePositive += self.matriz[row][classe]
        return falsePositive
    
    # Soma de todos os elementos excluíndo os da linha e coluna da tal classe
    def calculateTrueNegative(self, classe):
        trueNegative = 0
        for row in self.matriz:
            for column in self.matriz[row]:
                if row == classe or column == classe:
                    continue
                trueNegative += self.matriz[row][column]
        return trueNegative
    
    def calculateOverralAccuracy(self):
        diagonal = 0
        total = 0
        for row in self.matriz:
            for column in self.matriz:
                if row == column:
                    diagonal += self.matriz[row][column]
                total += self.matriz[row][column]
        return diagonal/total
                

    def getClassesRatings(self):
        return self.classesRatings


    def __str__(self):
        saida = ""
        for classe in self.classesRatings:
            saida += "************** Classe : " + str(classe['nome']) + " **************" + "\n"
            # saida += "Taxa de falso negativo: " + str(classe['falseNegative']) + "\n"
            # saida += "Taxa de falso positivo: " + str(classe['falsePositive']) + "\n"
            saida += "Taxa de verdadeiro positivo (Recall): " + "{:.3f}".format(str(classe['truePositive'])) + "\n"
            saida += "Taxa de verdadeiro negativo (Specificity): " + "{:.3f}".format(str(classe['trueNegative'])) + "\n"
            saida += "Acuracia: " + "{:.3f}".format(str(classe['accuracy'])) + "\n"
            saida += "Precisao: " + "{:.3f}".format(str(classe['precision'])) + "\n"
            saida += "F-Score:  " + "{:.3f}".format(str(classe['fScore'])) + "\n\n"
        saida += "Overral Accuracy: " + "{:.3f}".format(str(self.calculateOverralAccuracy()))
        return saida