if __name__ == '__main__':
    arquivos = []
    conteudo = []
    dicionario = {}
    nome = input('Digite o nome do arquivo a ser lido: ')
    encontrado = False
    try:
        arquivo = open('files/{}'.format(nome), 'r')
        encontrado = True
        for linha in arquivo.readlines():
            palavras = linha.split(' ')
            for palavra in palavras:
                conteudo.append('{}'.format(palavra[:-1]))
    except FileNotFoundError:
        print('Arquivo não encontrado')

    result = open('files/ocorrenciasdict.txt', 'w')
    for linha in conteudo:
        try:
            ocorrencia = conteudo.count(linha)
            dicionario[linha] = ocorrencia
        except ValueError:
            continue

    for valor in dicionario.items():
        print('{}'.format(valor))

    if encontrado:
        arquivo.close()
        result.close()
