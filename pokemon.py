class Pokemon:
    def __init__(self, tipo, especie):
        self.tipo = tipo
        self.especie = especie

    def __str__(self):
        return "{} ({})".format(self.especie,self.tipo)

    def atacar(self,pokemon):
        print("{} atacou {}!".format(self.especie, pokemon.especie))


