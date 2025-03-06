import requests

def get_pokemon_info(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        pokemon_info = {
            "Nom": data["name"],
            "ID": data["id"],
            "Taille": data["height"],
            "Poids": data["weight"],
            "Types": [t["type"]["name"] for t in data["types"]],
            "Statistiques": {stat["stat"]["name"]: stat["base_stat"] for stat in data["stats"]},
            "Capacités": [move["move"]["name"] for move in data["moves"]],
            "Image": data["sprites"]["front_default"]  # Ajout de l'image
        }
        return pokemon_info
    else:
        return {"Erreur": "Pokémon non trouvé"}

if __name__ == "__main__":
    pokemon_name = input("Entrez le nom d'un Pokémon : ")
    info = get_pokemon_info(pokemon_name)
    
    for key, value in info.items():
        print(f"{key}: {value}")
