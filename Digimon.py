#Classes
class Digimon:
    def __init__(self,nome,ataque = 1,defesa = 1,life = 100):
        self.nome = nome
        self.ataque = ataque
        self.defesa = defesa
        self.life = life

    def set_nome(self,nome):
        self.nome = nome

    def get_nome(self):
        return self.nome
		
    def __str__(self):
        return(" Nome  : %s \n Ataque: %i \n Defesa: %i \n Life  : %i"%(self.nome,self.ataque,self.defesa,self.life))
	
	def __cmp__(self, other):
		if (self.ataque > other.ataque): 
			return 1
		if (self.ataque < other.ataque):
			return -1
		return 0


