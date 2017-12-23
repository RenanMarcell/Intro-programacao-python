if __name__ == "__main__":
    open = 0
    closed = 0
    valido = True
    str = input("Digite os parenteses: \n")
    for letter in str:
        if letter == '(':
            open += 1
        elif letter == ')':
            if closed >= open:
                valido = False
            else:
                closed +=1

    if valido and open == closed:
        print('Entrada válida')
    else:
        print("Input inválido")
