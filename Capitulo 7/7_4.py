if __name__ == "__main__":
    str1 = input("Digite a primeira string: ")
    cont = {}
    str3 = ''
    for letter in str1:
        if letter not in str3:
            str3 += letter
            cont[letter] = 1
        else:
            cont[letter] += 1

    for letter, cont in cont.items():
        print('{}: {}x'.format(letter, cont))
