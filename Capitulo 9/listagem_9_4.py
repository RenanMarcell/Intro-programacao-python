if __name__ == '__main__':
    impares = open('files/impares.txt', 'w')
    pares = open('files/pares.txt', 'w')
    for n in range(0, 1000):
        if n % 2 == 0:
            pares.write('%d\n' % n)
        else:
            impares.write('%d\n' % n)

    impares.close()
    pares.close()

# Listagem necessária para fazer os exercícios
