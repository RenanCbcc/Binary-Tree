from Digimon import Digimon
from Node import Node
from Stack import Stack


class Tree:
    def __init__(self):
        self.root = None

    # ----------------------------------------------------------------------#
    def find(self, key):
        current = self.root
        while key != self.current.get_object():
            if current is None:
                return None
            elif key < self.current.get_object():
                current = self.current.get_left()
            else:
                current = self.current.get_right()
        return current


    def insert(self, name, xp):
        node = Node(Digimon(name, xp))
        if self.root is None:
            self.root = node
        else:
            current = self.root
            while True:
                parent = current  # parent sempre aponta para um nível acima
                if node.get_object() < current.get_object():  # vai pra esquerda?
                    current = current.get_left()
                    if current is None:
                        parent.set_left(node)  # insira na esquerda
                        return
                else:
                    current = current.get_right()  # vai pra direita?
                    if current is None:
                        parent.set_right(node)
                        return

    def delete(self, key):
        current = self.root
        isleftChild = True
        # se node for encontrado, sair do laço com o node a ser deletado
        while (current.get_object().get_xp() is not key):
            parent = current
            if key < current.get_object().get_xp():  # vai pra esquerda?
                isleftChild = True
                current = current.get_left()
            else:
                isleftChild = False
                current = current.get_right()

            if current is None:
                return False  # node não encontrado
        # fim do while

        ################################
        # Caso 1: o Node não tem filhos#
        ################################

        if current.is_leaf():

            if current is self.root:
                current = None  # árvore está vazia
            elif isleftChild:
                parent.set_left(None)
            else:
                parent.set_right(None)

        ############################################
        # Caso 2: o Node a ser deletado tem um filho#
        ############################################

        # se sem filho a direita, subustituir por subarvore da esquerda
        elif current.get_right() is None:
            if current is self.root:
                self.root = current.get_left()
            elif isleftChild:  # filho à esquerda do Node parent
                parent.set_left(current.get_left())
            else:
                parent.set_right(current.get_left())

        # se sem filho a esquerda, subustituir por subarvore da direita
        elif current.get_left() is None:
            if current is self.root:
                self.root = current.get_right()
            elif isleftChild:  # filho a esquerda de Node parent
                parent.set_left(current.get_right())
            else:
                parent.setDireita(current.get_right())

        ###############################################
        # Caso 3: o Node a ser deletado tem dois filho#
        ###############################################

        # para deletar um Node com dois filhos substitua o Node pelo seu successor se suscessor ehFolha
        # função successor() faz isso
        else:
            successor = self.successor(current)
            # conecta parent de current ao invéz de successor
            if current is self.root:
                root = successor
            elif isleftChild:
                parent.set_left(successor)
            else:
                parent.setDireita(successor)

            # conecta successor ao filho da esquerda do current
            successor.set_left(current.get_left())
        return True  # Fim delete()

    def quantity_nodes(self, no):
        if no is None:
            return 0
        quantity_left = self.quantity_nodes(no.get_left())
        quantity_right = self.quantity_nodes(no.get_right())
        return quantity_right + quantity_left + 1

    def in_order(self, root):  # visita os nos em ordem crescente
        if root is not None:
            self.in_order(root.get_left())
            print(root) # Or could be root.get_object() for mor details
            self.in_order(root.get_right())

    def minimum(self):
        print("Minimum value:")
        current = self.root
        while current is not None:
            parent = current
            current = current.get_left()
        print(parent)

    def maximum(self):
        print("Maximum value:")
        current = self.root
        while current is not None:
            parent = current
            current = current.get_right()
        print(parent)

    def successor(self, delNode):
        successor_parent = delNode
        successor = delNode
        current = delNode.get_right()
        while (current is not None):
            successor_parent = successor
            successor = current
            current = current.get_left()
            if successor is not delNode.get_right():
                successor_parent.set_left(successor_parent.get_right())
                successor.setDireita(delNode.get_right())

        return successor


# ----------------------------------------------------------------------#
tree = Tree()
tree.insert('Tentomon', 8)
tree.insert('Agumon', 10)
tree.insert('Greymon', 22)
tree.insert('Metal Greymon', 32)
tree.insert('War Greymon', 55)
tree.insert('Kabuterimon', 18)
tree.insert('Atlur Kabuterimon', 32)
tree.insert('Gabumon', 9)
tree.insert('Garurumon', 20)
tree.insert('Were Garurumon', 31)
tree.insert('Metal Garurumon', 50)

tree.in_order(tree.root)
tree.minimum()
tree.maximum()