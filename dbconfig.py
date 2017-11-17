import sqlite3

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

def create_database():
    conn = sqlite3.connect('database.db')
    conn.execute('CREATE TABLE IF NOT EXISTS Indicador (Id INTEGER, Nome TEXT, Porcentagem INTEGER, Peso REAL)')
    cur = conn.cursor()
    cur.execute('SELECT COUNT(*) FROM Indicador')
    rows = cur.fetchone()
    if (int(rows[0]) <= 0):
        conn.execute('INSERT INTO Indicador (Id, Nome, Porcentagem, Peso) VALUES (?, ?, ?, ?)', (1, 'ApisulLog 2.0', 0, 0.31))
        conn.execute('INSERT INTO Indicador (Id, Nome, Porcentagem, Peso) VALUES (?, ?, ?, ?)', (2, 'Integra 2.0', 0, 0.35))
        conn.execute('INSERT INTO Indicador (Id, Nome, Porcentagem, Peso) VALUES (?, ?, ?, ?)', (3, 'Multicadastro', 0, 0.17))
        conn.execute('INSERT INTO Indicador (Id, Nome, Porcentagem, Peso) VALUES (?, ?, ?, ?)', (4, 'ApisulCard', 0, 0.10))
        conn.execute('INSERT INTO Indicador (Id, Nome, Porcentagem, Peso) VALUES (?, ?, ?, ?)', (5, 'Reguladora', 0, 0.02))
        conn.execute('INSERT INTO Indicador (Id, Nome, Porcentagem, Peso) VALUES (?, ?, ?, ?)', (6, 'Integra 1.0', 0, 0.04))
        conn.execute('INSERT INTO Indicador (Id, Nome, Porcentagem, Peso) VALUES (?, ?, ?, ?)', (7, 'ApisulLog 1.0', 0, 0.01))
        conn.commit()
    conn.close()
    pass