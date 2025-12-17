import requests

def ejercicio4():
    url = "https://pokeapi.co/api/v2/pokemon"

    params = {
        "limit": 10,
        "offset": 0
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        # Convertir la respuesta a JSON 
        data = response.json()
    
        lista_pokemon = data.get("results", [])
        
        print(f"--- Listado de los primeros {len(lista_pokemon)} ---")
        
        for pokemon in lista_pokemon:
            print(f"Nombre: {pokemon['name']}")
    else:
        print(f"Error: {response.status_code}") 

if __name__ == "__main__":
    ejercicio4()