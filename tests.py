from concatenamento import Table
from openHash import OpenTable
import random
from timeit import default_timer as timer
import numpy as np
import csv
import matplotlib.pyplot as plt

def test(nstart, m, gap):

    row = ['alpha', 'openInsertTime', 'InsertTime', 'openCollisions', 'Collisions', 'searchOpenTime', 'searchTime', 'removeOpenTime', 'removeLinkedTime']
    with open('testInsert.csv', 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(row)
    csvFile.close()

    for n in range(nstart, int(m*0.95), gap):

        openInsertTimes = np.arange(10, dtype='f')
        insertTimes = np.arange(10, dtype='f')
        openInsertCollisions = np.arange(10)
        insertCollisions = np.arange(10)
        openSearchTimes = np.arange(10, dtype='f')
        searchTimes = np.arange(10, dtype='f')
        openRemoveTimes = np.arange(10, dtype='f')
        removeTimes = np.arange(10, dtype='f')

        for y in range(10):

            # creo le tabelle
            openTable = OpenTable(m)
            table = Table(m)

            # creo array dei valori da inserire
            values = np.arange(n)
            for i in range(n):
                k = random.randint(100000, 100000000)
                values[i] = k

            #scelgo valori da cercare e rimuovere
            removeValue = random.randint(100000, 100000000)
            searchValue = random.randint(100000, 100000000)

            # inserisco valori nella tabella a indirizzamento aperto
            startOpenInsert = timer()
            for x in values:
                openTable.openInsert(x)
            endOpenInsert = timer()
            openInsertTimes[y] = endOpenInsert - startOpenInsert
            openInsertCollisions[y] = openTable.collisioni

            #cerco nella tabella open
            startOpenSearch = timer()
            openTable.openSearch(searchValue)
            endOpenSearch = timer()
            openSearchTimes[y] = endOpenSearch - startOpenSearch

            #rimuovo dalla tabella open
            startOpenRemove = timer()
            openTable.openDelete(removeValue)
            endOpenRemove = timer()
            openRemoveTimes[y] = endOpenRemove - startOpenRemove

            # inserisco valori nella tabella con concatenamento
            startInsert = timer()
            for x in values:
                table.insert(x)
            endInsert = timer()
            insertTimes[y] = endInsert - startInsert
            insertCollisions[y] = table.collisioni

            # cerco nella tabella linked
            startSearch = timer()
            table.search(searchValue)
            endSearch = timer()
            searchTimes[y] = endSearch - startSearch

            # rimuovo dalla tabella linked
            startRemove = timer()
            table.delete(removeValue)
            endRemove = timer()
            removeTimes[y] = endRemove - startRemove

        openInsertTime = np.mean(openInsertTimes)
        insertTime = np.mean(insertTimes)
        openCollisions = np.mean(openInsertCollisions)
        collisions = np.mean(insertCollisions)
        searchOpenTime = np.mean(openSearchTimes)
        searchTime = np.mean(searchTimes)
        removeOpenTime = np.mean(openRemoveTimes)
        removeLinkedTime = np.mean(removeTimes)

        dataCsv = [n/m, openInsertTime, insertTime, openCollisions, collisions, searchOpenTime, searchTime, removeOpenTime, removeLinkedTime]
        with open('testInsert.csv', 'a') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(dataCsv)
        csvFile.close()

    data = np.loadtxt('testInsert.csv', delimiter=",", skiprows=1, usecols=[0, 1, 2, 3, 4, 5, 6, 7, 8])

    f = plt.figure(1)
    f.set_figheight(10)
    f.set_figwidth(10)
    plt.subplot(211)
    plt.plot(data[:, 0], data[:, 1], label='openInsert')
    plt.plot(data[:, 0], data[:, 2], label='insert')
    plt.xlabel('alpha')
    plt.ylabel('time(s)')
    plt.title("insert times")
    plt.legend()

    plt.subplot(212)
    plt.plot(data[:, 0], data[:, 3], label='openInsert')
    plt.plot(data[:, 0], data[:, 4], label='insert')
    plt.xlabel('alpha')
    plt.ylabel('collisions')
    plt.title("insert collisions")
    plt.legend()

    f = plt.figure(2)
    f.set_figheight(10)
    f.set_figwidth(10)
    plt.subplot(211)
    plt.plot(data[:, 0], data[:, 5], label='openInsert')
    plt.plot(data[:, 0], data[:, 6], label='insert')
    plt.xlabel('alpha')
    plt.ylabel('time(s)')
    plt.title("search times")
    plt.legend()

    plt.subplot(212)
    plt.plot(data[:, 0], data[:, 7], label='openInsert')
    plt.plot(data[:, 0], data[:, 8], label='insert')
    plt.xlabel('alpha')
    plt.ylabel('time(s)')
    plt.title("remove times")
    plt.legend()

    plt.show()
