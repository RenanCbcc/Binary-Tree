# Classe Digimon
class Digimon():
    def __init__(self, nome,xp):
        self.nome = nome
        self.ataque = 10
        self.defesa = 5
        self.life = 100
        self.xp = xp

    def set_nome(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome

    def getXp(self):
        return self.xp

    def __str__(self):
        return (" Nome  : %s \n Ataque: %i \n Defesa: %i " % (self.nome, self.ataque, self.defesa))

    def __lt__(self, dig):
        return self.getXp() < dig.getXp()

    def __eq__(self, dig):
        return self.getXp() == dig.getXp()

