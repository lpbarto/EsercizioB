from concatenamento import Table
from openHash import OpenTable
import random
from timeit import default_timer as timer


def main():
    m = 97169
    n = 10000
    tempoOpen = 0.0
    tempo = 0.0

    openTable = OpenTable(m)
    table = Table(m)
    for x in range(n):
        k = random.randint(100000, 100000000)
        startOpenInsert = timer()
        openTable.openInsert(k)
        endOpenInsert = timer()
        tempoOpen += (endOpenInsert - startOpenInsert)
        startInsert = timer()
        table.insert(k)
        endInsert = timer()
        tempo += (endInsert - startInsert)


    table.search(123456)
    print(openTable.collisioni)
    print(tempoOpen)
    print("")
    print(table.collisioni)
    print(tempo)

   # table.visit()
   # openTable.openVisit()



if __name__ == "__main__":
    main()
