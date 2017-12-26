if __name__ == '__main__':
    pagina = open('files/pagina.html', 'w', encoding="utf-8")
    pagina.write(
        """
        <!DOCTYPE html>
        <html lang="pt-br">
            <head>
                <meta charset="utf-8">
                <title> Titulo da pagina </title>
            </head>
            <body>
                Olá!
        """
    )
    for l in range(10):
        pagina.write("<p>%d</p>\n" % 1)
    pagina.write(
        """
            </body>
        </html>
        """
    )
    pagina.close()
