# Class Digimon
class Digimon:
    def __init__(self, name, xp):
        self.__name = name
        self.__attack = 10
        self.__defense = 5
        self.__life = 100
        self.__experience = xp

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def get_xp(self):
        return self.__experience

    def __str__(self):
        return " Name  : %s \n Attack: %i \n Defense: %i " % (self.__name, self.__attack, self.__defense)

    def __lt__(self, dig):
        return self.get_xp() < dig.get_xp()

    def __eq__(self, dig):
        return self.get_xp() == dig.get_xp()
