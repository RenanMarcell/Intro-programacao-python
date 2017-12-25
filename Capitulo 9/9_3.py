if __name__ == '__main__':
    impares = open('impares.txt', 'r')
    pares = open('pares.txt', 'r')
    paresimpares = open('pareseimpares.txt', 'w')
    str1 = pares.readlines()
    str2 = impares.readlines()
    for n in range(0, 500):
        paresimpares.write(str1[n])
        paresimpares.write(str2[n])

    impares.close()
    pares.close()
    paresimpares.close()
