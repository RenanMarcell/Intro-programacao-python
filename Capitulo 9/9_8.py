if __name__ == '__main__':
    nome = input('Digite o nome do arquivo a ser lido: ')
    arquivo = open('files/{}'.format(nome), 'r')
    arquivowrite = open('files/paginado_param.txt', 'w')
    caracteres_max = int(input("Digite o maximo de caracteres por linha: ")) - 1
    linhas_max = int(input("Digite o maximo de linhas por pagina: ")) - 2
    pagina = 1
    conteudo = []
    for idx, linha in enumerate(arquivo.readlines()):
        if len(linha) > caracteres_max:
            mult = 1
            carac = len(linha)
            while carac != 0:
                if len(linha[caracteres_max:]) > 0:
                    conteudo.append('{}\n'.format(linha[0:caracteres_max]))
                else:
                    conteudo.append('{}'.format(linha[0:caracteres_max]))
                linha = linha[caracteres_max:]
                mult = mult + 1
                carac = len(linha)
        else:
            conteudo.append('{}'.format(linha))

    for idx, linha in enumerate(conteudo):
        if idx % linhas_max == 0 and idx != 0:
            arquivowrite.write('{}\n'.format(pagina).center(caracteres_max))
            arquivowrite.write('paginado.txt\n\n'.center(16))
            pagina = pagina + 1
        else:
            arquivowrite.write(linha)
    arquivo.close()
    arquivowrite.close()
