if __name__ == "__main__":
    T = [-10, -8, 0, 1, 2, 5, -2, -4]
    maximo = T[0]
    minimo = T[0]
    summ = T[0]
    for temp in T[1:]:
        if temp > maximo:
            maximo = temp
        if minimo > temp:
            minimo = temp
        summ = summ + temp

    summ = summ / len(T)

    print('Temperatura minima %d' % minimo)
    print('Temperatura máxima %d' % maximo)
    print('Temperatura media %d' % summ)
