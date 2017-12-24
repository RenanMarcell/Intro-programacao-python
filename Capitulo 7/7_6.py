if __name__ == "__main__":
    str1 = input("Digite a primeira string: ")
    str2 = input("Digite a segunda string: ")
    str3 = input("Digite a terceira string[deve ter o mesmo tamanho da segunda]: ")
    while len(str3) != len(str2):
        str3 = input("Digite a terceira string[deve ter o mesmo tamanho da segunda]: ")

    dicionario = {}
    for idx, letter in enumerate(str2):
        dicionario[letter] = str3[idx]

    for letter in str2:
        if letter in str1:
            str1 = str1.replace(letter, dicionario[letter])

    print("Nova string: {}".format(str1))
