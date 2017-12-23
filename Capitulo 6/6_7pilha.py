if __name__ == "__main__":
    P = []
    valido = True
    str = input("Digite os parenteses: \n")
    for letter in str:
        if letter == '(':
            P.append(letter)
        elif letter == ')':
            try:
                P.pop(P.index('('))
            except ValueError:
                valido = False

    if valido and len(P) == 0:
        print("Expressão válida")
    else:
        print("Input inválido")
