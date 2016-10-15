# Classes
class Digimon():
    def __init__(self, nome, ataque=1, defesa=1, life=100,xp = 10):
        self.nome = nome
        self.ataque = ataque
        self.defesa = defesa
        self.life = life
        self.xp = xp

    def set_nome(self, nome):
        self.nome = nome

    def get_nome(self):
        return self.nome

    def __str__(self):
        return (
        " Nome  : %s \n Ataque: %i \n Defesa: %i \n Life  : %i \nXP : %i" % (self.nome, self.ataque, self.defesa, self.life,self.xp))

