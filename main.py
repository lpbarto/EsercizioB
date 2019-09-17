from concatenamento import LinkedList, hash
import numpy

def createTable(m):
    lista = LinkedList()
    table = [lista]
    for x in range(1, m, 1):
        lista = LinkedList()
        table.append(lista)
    return table

def main():
    m = 111
    k = 33325
    table = createTable(m)
    p = hash(k,m)
    print("hash %i" % p)
    table[p].add(k)
    print("inserito %i" % k)
    print(table[p].search(k))

if __name__ == "__main__":
    main()
