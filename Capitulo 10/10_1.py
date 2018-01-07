class Televisão:
    def __init__(self):
        self.ligada = False
        self.canal = 2
        self.tamanho = "32 polegadas"
        self.marca = "Samsung"


if __name__ == '__main__':
    tv_sala = Televisão()
    tv = Televisão()
    tv_sala.canal = 4
    tv_sala.ligada = True
    print(tv_sala)
    print(tv_sala.ligada)
    print(tv_sala.canal)
    print(tv_sala.marca)
    print(tv_sala.tamanho)
