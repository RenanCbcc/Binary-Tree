from Digimon import Digimon
from Node import Node

class Tree():
    def __init__(self):
        self.raiz = None

    def find(self,chave):
        atual = self.raiz
        while(chave != self.atual.obj.getXp()):
            if atua is None:
                return None
            elif chave < self.atual.obj.getXp():
                atual = self.atual.getEsquerda()
            else:
                atual = self.atual.getDireita()
        return atual


    def insert(self,digimon,Xp):
        no = Node(Digimon(digimon,Xp))
        if self.raiz is None:
            self.raiz = no
        else:
            atual = self.raiz
            while(True):
                pai = atual # pai sempre aponta para um nível acima
                if no.obj < atual.obj : # vai pra esquerda?
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
        pass


    def inOrder(self,raiz):# visita os nos em ordem crescente
        if raiz is not None:
            self.inOrder(raiz.getEsquerda())
            print(raiz.obj.xp,raiz.obj.nome)
            self.inOrder(raiz.getDireita())

    def minimun(self):
        atual = self.raiz
        while(atual is not None):
            pai = atual
            atual = atual.getEsquerda()
        print( pai )


    def maximun(self):
        atual = self.raiz
        while (atual is not None):
            pai = atual
            atual = atual.getDireita()
        print( pai )

    def sucessor(self,delNode):
        sucessorPai = delNode
        sucessor = delNode
        atual = delNode.getDireita()
        while( atual is not None):
            sucessorPai = sucessor
            sucessor = atual
            atual = atual.getEsquerda()
            if sucessor is not delNode.getDireita():
                sucessorPai.setEsquerda(sucessorPai.getDireita())
                sucessor.setDireita(delNode.getDireita())

        return sucessor

#----------------------------------------------------------------------#
tree = Tree()
tree.insert('Tentomon',8)
tree.insert('Agumon',10)
tree.insert('Greymon',22)
tree.insert('Metal Greymon',32)
tree.insert('War Greymon',55)
tree.insert('Kabuterimon',18)
tree.insert('Atlur Kabuterimon',32)
tree.insert('Gabumon',9)
tree.insert('Garurumon',20)
tree.insert('Were Garurumon',31)
tree.insert('Metal Garurumon',50)
