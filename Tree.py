from Digimon import Digimon
from Node import Node

class Tree():
    def __init__(self):
        self.raiz = None

    def find(self,chave):
        atual = self.raiz
        while(chave != self.raiz.obj.ataque):
            if atua is None:
                return None
            elif chave < self.raiz.obj.ataque:
                atual = self.raiz.getEsquerda()
            else:
                atual = self.raiz.getDireita()
        return atual


    def insert(self,digimon):
        no = Node(digimon)
        if self.raiz is None:
            self.raiz = no
        else:
            atual = self.raiz
            while(True):
                pai = atual # pai sempre aponta para um nível acima
                if no.obj.ataque < pai.obj.ataque: # vai pra esquerda?
                    atual = atual.getEsquerda()
                    if atual is None:
                        pai.setEsquerda(no) #insira na esquerda
                        return
                else:
                    atual = atual.getDireita()  # vai pra direita?
                    if atual is None:
                        pai.setDireita(no)
                        return

    def delete(self,chave):
        atual = self.raiz
        while(chave != atual.obj.ataque):
            pai = atual
            if chave < atual.obj.ataque:
                atual = atual.getEsquerda()
                if atual is None:


    def inOrder(self,raiz):# visita os nos em ordem crescente
        if raiz is not None:
            self.inOrder(raiz.getEsquerda())
            print(raiz.obj.ataque,raiz.obj.nome)
            self.inOrder(raiz.getDireita())

    def minimun(self):
        atual = self.raiz
        while(atual is not None):
            pai = atual
            atual = atual.getEsquerda()
        return pai


    def maximun(self):
        atual = self.raiz
        while (atual is not None):
            pai = atual
            atual = atual.getDireita()
        return pai
