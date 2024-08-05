class Node:
    def __init__(self, _data):
        self.data = _data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    # Imprime todos os elementos no formato [1,2,3]
    def print(self):
        aux = self.first
        print("[", end='')
        for i in range(self.size):
            print(aux.data, end='')
            if aux.next is not None: print(",", end='')
            aux = aux.next
        print("]")
    
    # Insere o elemento na última posição
    def pushBack(self, e) -> bool:
        aux = Node(e)
        if self.first is None:
            self.first = self.last = aux
        else:
            self.last.next = aux 
            aux.prev = self.last
            self.last = aux
        self.size += 1
        return True

    # Insere o elemento na primeira posição
    def pushFront(self, e) -> bool:
        aux = Node(e)
        if self.first is None:
            self.last = self.first = aux
        else:
            self.first.prev = aux
            aux.next = self.first
            self.first = aux
        self.size += 1
        return True

    # Insere o elemento na posição pos
    def insert(self, pos: int, e) -> bool:
        if pos < 0: return False
        if pos > self.size: return False
        if self.empty():
            return self.pushBack(e)
        elif pos == 0:
            return self.pushFront(e)
        elif pos == self.size:
            return self.pushBack(e)
        else:
            new = Node(e)
            if pos < self.size/2:
                aux = self.first
                for i in range(pos-1): aux = aux.next
            else:
                aux = self.last
                for i in range(self.size, pos, -1): aux = aux.prev
            new.next = aux.next
            new.prev = aux
            aux.next.prev = new
            aux.next = new
            self.size += 1
            return True

    # Remove o último elemento
    def popBack(self):
        if self.first is None: return False
        aux = self.first.data
        if self.size == 1:
            self.first = self.last = None
        else:
            self.last = self.last.prev
            self.last.next = None
        self.size -= 1
        return aux

    # Remove o primeiro elemento
    def popFront(self):
        if self.first is None: return False
        aux = self.last.data
        if self.size == 1:
            self.first = self.last = None
        else:
            self.first = self.first.next
            self.first.prev = None
        self.size -= 1
        return aux

    # Remove o elemento da posição pos e retorna o elemento removido
    def erase(self, pos: int):
        if self.first is None: return False
        if pos < 0: return False
        if pos >= self.size: return False
        if pos == 0:
            return self.popFront()
        elif pos == self.size:
            return self.popBack()
        else:
            if pos < self.size/2:
                aux = self.first
                for i in range(pos): aux = aux.next
            else:
                aux = self.last
                for i in range(self.size, pos+1, -1): aux = aux.prev
            knot = aux.next
            knot.prev = aux.prev
            aux.prev.next = knot
            self.size -= 1
            return aux.data

    # Retorna o primeiro elemento
    def front(self):
        if self.first is not None: return self.first.data

    # Retorna o último elemento
    def back(self):
        if self.last is not None: return self.last.data

    # Retorna o elemento da posição pos
    def at(self, pos: int):
        if pos < 0 or pos >= self.size: return False
        if pos < self.size/2:
            aux = self.first
            for i in range(pos): aux = aux.next
        else: 
            aux = self.last
            for i in range(self.size, pos+1, -1): aux = aux.prev
        return aux.data

    # Torna a lista vazia
    def clear(self):
        self.first.next.prev = None
        self.last.prev.next = None
        self.first = self.last = None
        self.size = 0

    # Verifica se o vetor está vazio
    def empty(self):
        return self.size == 0

    # Devolve a quantidade de elementos
    def getSize(self) -> int:
        return self.size

    # Substitui o elemento da posição pos pelo elemento e
    def replace(self, pos, e):
        if pos < 0 or pos >= self.size: return False
        if pos < self.size/2:
            aux = self.first
            for i in range(pos): aux = aux.next
        else: 
            aux = self.last
            for i in range(self.size, pos+1, -1): aux = aux.prev
        aux.data = e
        return True

def main():
    linkedlist = DoublyLinkedList()
    linkedlist.pushBack(1)
    linkedlist.pushBack(2)
    linkedlist.pushBack(3)
    linkedlist.pushFront(2)
    linkedlist.pushFront(3)
    linkedlist.pushFront(1)
    linkedlist.insert(5, 10)
    linkedlist.insert(2, 15)
    linkedlist.insert(0, 20)
    linkedlist.print()
    linkedlist.erase(3)
    linkedlist.print()
    linkedlist.clear()
    linkedlist.pushBack(1)
    linkedlist.pushBack(2)
    linkedlist.pushBack(3)
    linkedlist.pushFront(2)
    linkedlist.pushFront(3)
    linkedlist.pushFront(1)
    linkedlist.insert(5, 10)
    linkedlist.insert(2, 15)
    linkedlist.insert(0, 20)
    print(linkedlist.at(7))
    linkedlist.print()
    linkedlist.replace(3, 50)
    linkedlist.print()
main()