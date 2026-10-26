import requests

base_url = "https://pokeapi.co/api/v2"


def get_pokemon_info(pokemon_name):
    pokemon_name = pokemon_name.strip().lower()
    if not pokemon_name:
        print("Please enter a Pokémon name.")
        return

    url = f"{base_url}/pokemon/{pokemon_name}"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 404:
            print(f"Error: Pokémon '{pokemon_name}' not found.")
            return
        response.raise_for_status()
        data = response.json()
    except requests.RequestException as error:
        print(f"Could not retrieve Pokémon information: {error}")
        return

    print(f"Name: {data['name']}")
    print(f"ID: {data['id']}")
    print(f"Height: {data['height']}")
    print(f"Weight: {data['weight']}")
    print("Types:")

    for type_info in data['types']:
        print(f"- {type_info['type']['name']}")


if __name__ == "__main__":
    pokemon_name = input("Enter the name of the Pokémon: ")
    get_pokemon_info(pokemon_name)