import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'Your_Trainer_Token'
HEADER = {'Content-Type': 'application/json', 'trainer_token' : TOKEN}

body_pokemon_maker = {
    "name": "ZULAZAVR",
    "photo_id": 45
}

body_pokemon_change = {
    "pokemon_id": "178088",
    "name": "POPOZAVR",
    "photo_id": 45
}
pokemon_catch = {
    "pokemon_id": "178088"
}

response_task_1 = requests.post(url=f'{URL}/pokemons', headers=HEADER, json=body_pokemon_maker)

print(response_task_1.text)

response_task_2 = requests.put(url=f'{URL}/pokemons', headers=HEADER, json=body_pokemon_change)

print(response_task_2.text)

response_task_3 = requests.post(url=f'{URL}/trainers/add_pokeball', headers=HEADER, json=pokemon_catch)

print(response_task_3.text)