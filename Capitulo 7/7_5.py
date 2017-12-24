if __name__ == "__main__":
    str1 = input("Digite a primeira string: ")
    str2 = input("Digite a segunda string: ")
    for letter in str2:
        if letter in str1:
            str1 = str1.replace(letter, '')

    print("Nova string: {}".format(str1))
