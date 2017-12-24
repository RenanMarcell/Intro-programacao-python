if __name__ == "__main__":
    str1 = input("Digite a primeira string: ")
    str2 = input("Digite a segunda string: ")
    if str2.find(str1) >= 0:
        print("String achada na posição {}".format(str2.find(str1)))
    else:
        print("String 1 não está dentro da string 2")
