def hash(k, m):
    return k % m

class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None
    def get_data(self):
        return self.data
    def get_next(self):
        return self.next
    def set_data(self, new_data):
        self.data = new_data
    def set_next(self, new_next):
        self.next = new_next

class LinkedList:
    def __init__(self):
        self.head = None
    def is_empty(self):
        return self.head == None
    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        testa = self.head
        self.head = temp
        if testa is None:
            return 0
        else:
            return 1
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.get_next()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found

    def PrintL(self):
        current = self.head
        previous = None
        while current != None:
            print('..',  current.get_data(), end= '')
            current = current.get_next()

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current is not None:
                if current.get_data() == item:
                    found = True
                else:
                    previous = current
                    current = current.get_next()
            else:
                return found
        if previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
        return found

class Table:
    def __init__(self, m):
        self.collisioni = 0
        self.size = m
        lista = LinkedList()
        table = [lista]
        for x in range(1, m, 1):
            lista = LinkedList()
            table.append(lista)
        self.table = table

    def insert(self, k):
        h = hash(k, self.size)
        self.collisioni += self.table[h].add(k)
        #print("chiave %i, posizione %i" %(k, h))

    def visit(self):
        for x in range(0, self.size, 1):
            self.table[x].PrintL()
            print(" ")

    def delete(self, k):
        h = hash(k, self.size)
        self.table[h].remove(k)
        '''
        if self.table[h].remove(k):
            print("rimossa chiave %i" % k)
        else:
            print("chiave %i non trovata" % k)
        '''

    def search(self, k):
        h = hash(k, self.size)
        self.table[h].search(k)
        '''
        if self.table[h].search(k):
            print("chiave %i trovata" % k)
        else:
            print("chiave %i non trovata" % k)
        '''


