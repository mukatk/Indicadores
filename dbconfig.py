#import sqlite3

#conn.execute('CREATE TABLE Indicador (Nome TEXT, Porcentagem INTEGER, Peso REAL)')


#conn.execute('INSERT INTO Indicador (Nome, Porcentagem, Peso) VALUES (?, ?, ?)', ('ApisulLog 2.0', 0, 0.31))
#conn.execute('INSERT INTO Indicador (Nome, Porcentagem, Peso) VALUES (?, ?, ?)', ('Integra 2.0', 0, 0.35))
#conn.execute('INSERT INTO Indicador (Nome, Porcentagem, Peso) VALUES (?, ?, ?)', ('Multicadastro', 0, 0.17))
#conn.execute('INSERT INTO Indicador (Nome, Porcentagem, Peso) VALUES (?, ?, ?)', ('ApisulCard', 0, 0.10))
#conn.execute('INSERT INTO Indicador (Nome, Porcentagem, Peso) VALUES (?, ?, ?)', ('Reguladora', 0, 0.02))
#conn.execute('INSERT INTO Indicador (Nome, Porcentagem, Peso) VALUES (?, ?, ?)', ('Integra 1.0', 0, 0.04))
#conn.execute('INSERT INTO Indicador (Nome, Porcentagem, Peso) VALUES (?, ?, ?)', ('ApisulLog 1.0', 0, 0.01))

#conn = sqlite3.connect('database.db')
#cur = conn.cursor()
#cur.execute('SELECT * FROM Indicador')
#rows = cur.fetchall()
#for row in rows:
#    print(row)
#conn.close()