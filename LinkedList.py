class Knot:
    def __init__(self, data, prev, next):
        self.data = data
        self.prev = prev
        self.next = next

class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = None

    # Imprime todos os elementos no formato [1,2,3]
    def __str__(self):
        pass
    
    # Insere o elemento na última posição
    def pushBack(self, e) -> bool:
        pass

    # Insere o elemento na primeira posição
    def pushFront(self, e) -> bool:
        pass

    # Insere o elemento na posição pos
    def insert(self, pos, e) -> bool:
        pass

    # Remove o último elemento
    def popBack(self):
        pass

    # Remove o primeiro elemento
    def popFront(self):
        pass

    # Remove o elemento da posição pos e retorna o elemento removido
    def erase(self, pos):
        pass

    # Retorna o primeiro elemento
    def front(self):
        pass

    # Retorna o último elemento
    def back(self):
        pass

    # Retorna o elemento da posição pos
    def at(self, pos):
        pass

    # Torna a lista vazia
    def clear(self):
        pass

    # Verifica se o vetor está vazio
    def empty(self) -> bool:
        pass

    # Devolve a quantidade de elementos
    def getSize(self) -> int:
        pass

    # Substitui o elemento da posição pos pelo elemento e
    def replace(self, pos, e):
        pass






def main():
    linkedlist = LinkedList()
    linkedlist.pushBack(1)

main()