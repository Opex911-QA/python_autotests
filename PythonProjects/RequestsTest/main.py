import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'b556f05ef999c31e7b15671151f1c950'
HEADER1 = {'Content-Type' : 'application/json'}
HEADER2 = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

body_reg = {
    "trainer_token": TOKEN,
    "email": "E-mail",
    "password": "Password"
}
body_conf = {
    "trainer_token": TOKEN
}
body_create = {
    "name": "generate",
    "photo_id": -1
}

# Регистрация и активация тренера
# response = requests.post(url=f'{URL}/trainers/reg', headers=HEADER1, json=body_reg)
# print(response.text) Тренер зарегистрирован уже
# response_conf = requests.post(url=f'{URL}/trainers/confirm_email', headers=HEADER1, json=body_conf)
# print(response_conf.text) и подтвержден

# Действия с покемонами
response_create = requests.post(url=f'{URL}/pokemons', headers=HEADER2, json=body_create)
print(response_create.text)
pokemon_id = response_create.json()['id']
print(pokemon_id)

body_change = {
    "pokemon_id": pokemon_id,
    "name": "generate",
    "photo_id": -1
}
body_catch = {
    "pokemon_id": pokemon_id
}
body_knockout = {
    "pokemon_id": "43421"
}


response_change = requests.put(url=f'{URL}/pokemons', headers=HEADER2, json=body_change)
print(response_change.text)
response_catch = requests.post(url=f'{URL}/trainers/add_pokeball', headers=HEADER2, json=body_catch)
print(response_catch.text)
# response_knockout = requests.post(url=f'{URL}/pokemons/knockout', headers=HEADER2, json=body_knockout)
# print(response_knockout.text) Борьба с перенаселением покемонов
