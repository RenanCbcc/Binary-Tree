import Digimon

class Node():
    def __init__(self,Digimom):
        self.obj = Digimon
        self.esquerda = None  #left chield
        self.direita = None     #right chield

    def getEsquerda(self):
        return self.esquerda

    def setEsquerda(self,no):
        self.esquerda = no

    def getDireita(self):
        return self.direita

    def setDireita(self,no):
        self.direita = no


