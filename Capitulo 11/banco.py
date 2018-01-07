import sqlite3
from contextlib import closing


conexao = sqlite3.connect('precos.db')
cursor = conexao.cursor()
cursor.execute('SELECT * from precos where preco > 30 and preco < 41')
resultado = cursor.fetchone()
print("Nome do produto: %s\nPreço: %s" % resultado)
conexao.commit()
cursor.close()
conexao.close()
