class Indicador:
    def __init__(self, nome, porcentagem, peso):
        self.Nome = nome
        self.Porcentagem = porcentagem
        self.Peso = peso
    def serialize(self):
        return {
            'Nome': self.Nome,
            'Porcentagem': self.Porcentagem,
            'Peso': self.Peso
        }