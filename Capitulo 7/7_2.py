if __name__ == "__main__":
    str1 = input("Digite a primeira string: ")
    str2 = input("Digite a segunda string: ")
    str3 = ''
    for letter in str1:
        if letter in str2 and letter not in str3:
            str3 += letter

    print("Letras em comum em ambas strings: {}".format(str3))
