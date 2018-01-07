import random


if __name__ == '__main__':
    n = random.randint(1, 10)
    x = int(input("Escolha um numero entre 1 e 10: "))
    chances = 0
    while chances < 3:
        if x == n:
            print("Você acertou")
            break
        else:
            print("Você errou")

        print("Tentativa {} de 3, numero correto era {}".format(chances+1, n))
        chances += 1
        n = random.randint(1, 10)
