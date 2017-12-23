if __name__ == "__main__":
    dicionario = {}
    frase = "O rato"
    for letter in frase:
        if letter != ' ':
            dicionario[letter] = 1

    print(dicionario)
