if __name__ == '__main__':
    nome = input('Digite o nome do arquivo a ser lido: ')
    arquivo = open('files/{}'.format(nome), 'r')
    arquivowrite = open('files/paginado.txt', 'w')
    pagina = 1
    conteudo = []
    for idx, linha in enumerate(arquivo.readlines()):
        if len(linha) > 75:
            mult = 1
            carac = len(linha)
            while carac != 0:
                if len(linha[75:]) > 0:
                    conteudo.append('{}\n'.format(linha[0:75]))
                else:
                    conteudo.append('{}'.format(linha[0:75]))
                linha = linha[75:]
                mult = mult + 1
                carac = len(linha)
        else:
            conteudo.append('{}'.format(linha))

    for idx, linha in enumerate(conteudo):
        if idx % 58 == 0 and idx != 0:
            arquivowrite.write('{}\n'.format(pagina).center(75))
            arquivowrite.write('paginado.txt\n\n'.center(16))
            pagina = pagina + 1
        else:
            arquivowrite.write(linha)
    arquivo.close()
    arquivowrite.close()
