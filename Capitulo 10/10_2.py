class Televisão:
    def __init__(self, atual, c_min=2, c_max=14):
        self.ligada = False
        self.canal = atual
        self.tamanho = "32 polegadas"
        self.marca = "Samsung"
        self.cmin = c_min
        self.cmax = c_max

    def muda_canal_para_cima(self):
        if self.canal+1 < self.cmax:
            self.canal += 1
        elif self.canal + 1 == self.cmax:
            self.canal = self.cmin + 1

    def muda_canal_para_baixo(self):
        if self.canal-1 > self.cmin:
            self.canal -= 1
        elif self.canal - 1 == self.cmin:
            self.canal = self.cmax - 1


if __name__ == '__main__':
    tv_sala = Televisão(5)
    tv = Televisão(7, c_min=0, c_max=20)
    tv_sala.ligada = True
    opcao = input('Mudar canal para [cima] ou [baixo] [fim para acabar]:')
    while opcao.lower() != 'fim':
        if opcao == 'cima':
            tv.muda_canal_para_cima()
            print(tv.canal)
        elif opcao == 'baixo':
            tv.muda_canal_para_baixo()
            print(tv.canal)
        else:
            print("Entrada invalida.")

        opcao = input('Mudar canal para [cima] ou [baixo] [fim para acabar]:')

    print(tv_sala.ligada)
    print(tv_sala.canal)
    print(tv_sala.marca)
    print(tv_sala.tamanho)

# Também é o 10_3/4/5.py
