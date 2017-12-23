if __name__ == "__main__":
    ultimo = 10
    fila1 = list(range(1, ultimo+1))
    fila2 = list(range(1, ultimo+1))
    while True:
        print("\nExistem %d clientes na fila1 e %d clientes na fila2" % (len(fila1), len(fila2)))
        print("Filas atuais: ", fila1, fila2)
        print("Digite F/G para adicionar um cliente aos finais das filas, ")
        print("ou A/B para realizar o atendimento. S para sair.")
        operacao = input("Operação (F,G,A,B ou S): ")
        for letter in operacao:
            if letter == "A":
                if len(fila1) > 0:
                    atendido = fila1.pop()
                    print("Cliente %d da fila1 atendido" % atendido)
                else:
                    print("Fila vazia! Ninguém para atender.")
            elif letter == "B":
                if len(fila2) > 0:
                    atendido = fila2.pop()
                    print("Cliente %d da fila2 atendido" % atendido)
                else:
                    print("Fila vazia! Ninguém para atender.")
            elif letter == "F":
                ultimo += 1
                fila1.append(ultimo)
            elif letter == "G":
                ultimo += 1
                fila2.append(ultimo)
            elif letter == "S":
                break
            else:
                print("Operação inválida! Digite apenas F, G, A, B ou S")
        if operacao[-1] == 'S':
            break
