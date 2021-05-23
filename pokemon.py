class Pokemon:
    def __init__(self, tipo, especie,level=1, nome=None):
        self.tipo = tipo
        self.especie = especie
        self.level = level
        self.nome = nome

    def __str__(self):
        return "{} ({})".format(self.nome,self.level)

    def atacar(self,pokemon):
        print("{} atacou {}!".format(self.especie, pokemon.especie))

class PokemonEletrico(Pokemon):
    def atacar(self,pokemon):
        print("{} lancou um raio do trovao em {}".format(self,pokemon))
