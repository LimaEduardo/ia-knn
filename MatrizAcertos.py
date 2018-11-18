# Classe com a quantidade de acertos de uma classe
# Apesar do nome, não se usa uma matriz
from prettytable import PrettyTable

class MatrizAcertos:
    def __init__(self, negativoNegativo, negativoPositivo, positivoNegativo, positivoPositivo):
        self.negativoNegativo = negativoNegativo
        self.negativoPositivo = negativoPositivo
        self.positivoNegativo = positivoNegativo
        self.positivoPositivo = positivoPositivo

    def __str__(self):
        saida = PrettyTable()
        saida.field_names = ["", "Negativo", "Positivo"]
        saida.add_row(["Negativo", self.negativoNegativo, self.negativoPositivo])
        saida.add_row(["Positivo", self.positivoNegativo, self.positivoPositivo])
        return saida.__str__()
        