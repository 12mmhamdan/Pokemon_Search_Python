import requests

class Pokemon:
    def __init__(self, name, height, weight):
        self.name=name
        self.height=height
        self.weight=weight

    def __str__(self):
        output = f"----{self.name.title()}----\n"
        output += f"Height: {self.height}\n"
        output += f"Weight: {self.weight} \n"
        return output
    
    def __repr__(self):
        return(f"<Pokemon | {self.name}>")


class PokemonAPI:
    def __init__(self):
        self.base_url= "https://pokeapi.co/api/v2/pokemon/"

    
    def __get(self, poke_name):

        res = requests.get(f"{self.base_url}{poke_name}")
        if res.ok:
            return res.json()
        return f"{poke_name} isn't a pokemon!"


    def get_pokemon(self, pokemon_name):
        data = self.__get(pokemon_name)
        if pokemon_name in data:
            return f'{pokemon_name.title()} isnt a pokemon!'
        else:
            name = data['name']
            height = data['height']
            weight = data['weight']
            new_pokemon = Pokemon(name,height,weight)
            return new_pokemon
    
    
        
pokemon1 = PokemonAPI()
new = pokemon1.get_pokemon('charizard')
print(new)

pokemon2 = PokemonAPI()
new2 = pokemon2.get_pokemon('cherrymon')
print(new2)

