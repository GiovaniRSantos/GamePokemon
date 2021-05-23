from pokemon import *

class Pessoa:
    def __init__(self, nome=None, pokemons=[]):
        if nome:
            self.nome = nome
        else:
            self.nome = "Anonimo"

        self.pokemons = pokemons

    def __str__(self):
        return self.nome


    def mostrar_pokemons(self):
        if self.pokemons:
            for pokemon in self.pokemons:
                print(pokemon)


class Player(Pessoa):
    tipo = "Player"
    def capturar(self, pokemon):
        self.pokemons.append(pokemon)


class Inimigo(Pessoa):
    tipo = "Inimigo"


eu = Player("Giovani")

pokemon_selvagem = PokemonFogo("charmander")
eu.mostrar_pokemons()

eu.capturar(pokemon_selvagem)
eu.mostrar_pokemons()