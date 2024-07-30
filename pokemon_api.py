import requests

def fetch_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve data for {pokemon_name}")
        return None

def calculate_average_weight(pokemon_list):
    total_weight = 0
    for pokemon in pokemon_list:
        total_weight += pokemon['weight']
    return total_weight / len(pokemon_list)


pokemon_names = ["pikachu", "bulbasaur", "charmander"]
pokemon_data_list = []

for name in pokemon_names:
    data = fetch_pokemon_data(name)
    if data:
        pokemon_data_list.append(data)

if pokemon_data_list:
    
    for pokemon in pokemon_data_list:
        print("Name:", pokemon['name'])
        print("Abilities:", [ability['ability']['name'] for ability in pokemon['abilities']])
        print("Weight:", pokemon['weight'])
        print("-----")

    average_weight = calculate_average_weight(pokemon_data_list)
    print("Average Weight:", average_weight)
