class Pokemon:
    def __init__(self, especie,level=1, nome=None):
        self.especie = especie
        self.level = level
        self.nome = nome

    def __str__(self):
        return "{} ({})".format(self.nome,self.level)

    def atacar(self,pokemon):
        print("{} atacou {}!".format(self.especie, pokemon.especie))

class PokemonEletrico(Pokemon):
    tipo = "eletrico"

    def atacar(self,pokemon):
        print("{} lancou um raio do trovao em {}".format(self,pokemon))


class PokemonFogo(Pokemon):
    tipo = "fogo"

    def atacar(self,pokemon):
        print("{} lancou uma bola de fogo em {}".format(self,pokemon))

class PokemonAgua(Pokemon):
    tipo = "agua"

    def atacar(self,pokemon):
        print("{} lancou um jato de agua em {}".format(self,pokemon))

class PokemonVeveno(Pokemon):
    tipo = "veneno"

    def atacar(self,pokemon):
        print("{} lancou um veneno em {}".format(self,pokemon))
