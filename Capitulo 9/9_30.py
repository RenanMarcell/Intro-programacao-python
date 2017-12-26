if __name__ == '__main__':
    filmes = {
        'drama': ["Cidadão Kane", "O poderoso chefão"],
        'comédia': ["Tempos modernos", 'American Pie', 'Dr. Dolittle'],
        'policial': ["Chuva negra", 'Desejo de matar', 'Difícil de matar'],
        'guerra': ["Rambo", "Platoon", 'Tora!Tora!Tora!']
    }
    pagina = open('files/filmesUL.html', 'w', encoding="utf-8")
    pagina.write(
        """
        <!DOCTYPE html>
        <html lang="pt-br">
            <head>
                <meta charset="utf-8">
                <title>Filmes</title>
            </head>
            <body>
        """
    )
    for c, v in filmes.items():
        pagina.write("<ul>%s\n" % c)
        for e in v:
            pagina.write("<li>%s</li>" % e)
        pagina.write('</ul>')

    pagina.write(
        """
            </body>
        </html>
        """
    )
    pagina.close()
