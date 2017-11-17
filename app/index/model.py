import sqlite3, os

class Indicador:
    def __init__(self, id, nome, porcentagem, peso):
        self.Id = id
        self.Nome = nome
        self.Porcentagem = porcentagem
        self.Peso = peso
    def serialize(self):
        return {
            'Id': self.Id,
            'Nome': self.Nome,
            'Porcentagem': self.Porcentagem,
            'Peso': self.Peso
        }

class db_indicador:
    caminho_banco = os.path.abspath('database.db')
    def busca_indicadores(self):
        conn = sqlite3.connect(self.caminho_banco)
        cur = conn.cursor()
        cur.execute('SELECT * FROM Indicador')
        rows = cur.fetchall()
        conn.close()
        return [Indicador(row[0], row[1], row[2], row[3]) for row in rows]
    def atualiza_indicador(self, id, porcentagem):
        conn = sqlite3.connect(self.caminho_banco)
        conn.execute('UPDATE Indicador SET Porcentagem = ? WHERE Id = ?', (porcentagem, id))
        conn.commit()
        conn.close()