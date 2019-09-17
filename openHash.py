DELETED = 'DELETED'

def hash(k, i, m):
    h = k % m
    return (h+i) % m

class OpenTable:
    def __init__(self, m):
        self.size = m
        openTable = [None]
        for x in range(1, m, 1):
            openTable.append(None)
        self.openTable = openTable
        self.collisioni = 0

    def openInsert(self, k):
        i = 0
        while i < self.size:
            j = hash(k, i, self.size)
            if self.openTable[j] is None or self.openTable[j] is DELETED:
                self.openTable[j] = k
                #print("chiave %i, posizione %i" %(k , j))
                self.collisioni += i
                return
            else:
                i += 1
        #print("hash table overflow")

    def openDelete(self, k):
        i = 0
        while i < self.size:
            j = hash(k, i, self.size)
            if self.openTable[j] == k:
                self.openTable[j] = DELETED
                print("chiave %i posizione %i eliminata" %(k, j))
                return
            else:
                i += 1
        print("key not found")

    def openSearch(self, k):
        i = 0
        while i < self.size:
            j = hash(k, i, self.size)
            if self.openTable[j] == k:
                print("trovata chiave %i posizione %i" %(k, j))
                return
            elif self.openTable[j] is None:
                print("Non trovata chiave %i " % k)
                return None
            else:
                i += 1
        print("Non trovata chiave %i " % k)
        return None

    def openVisit(self):
        for x in range(0, self.size, 1):
            print(self.openTable[x])




