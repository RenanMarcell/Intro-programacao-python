if __name__ == '__main__':
    arquivos = []
    conteudo = []
    while True:
        nome = input('Digite o nome dos arquivos a serem lidos[fim para parar]: ')
        if nome.lower() == 'fim':
            break
        else:
            arquivos.append(nome)

    if len(arquivos) > 0:
        encontrado = False
        for nomes in arquivos:
            try:
                arquivo = open('files/{}'.format(nomes), 'r')
                encontrado = True
                for linha in arquivo.readlines():
                    conteudo.append('{}'.format(linha))
            except FileNotFoundError:
                print('Arquivo não encontrado')

        result = open('files/somalista.txt', 'w')
        for linha in conteudo:
            result.write(linha)
        if encontrado:
            arquivo.close()
            result.close()
    else:
        print('Lista de nomes vazia')
