if __name__ == '__main__':
    pares = open('files/pares.txt', 'r')
    paresinv = open('files/paresinvertido.txt', 'w')
    str1 = pares.readlines()
    str1 = str1[::-1]
    for n in range(0, len(str1)):
        paresinv.write(str1[n])

    pares.close()
    paresinv.close()
