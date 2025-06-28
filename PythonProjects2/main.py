import requests
import json

# Конфигурация
TRAINER_TOKEN = "абвг"  # Замените на ваш токен
TRAINER_ID = "1234"  # Замените на ваш ID тренера
BASE_URL = "https://api.pokemonbattle.ru/v2"

# 1. Создание покемона (POST /pokemons)
print("1. Создание покемона:")
create_url = f"{BASE_URL}/pokemons"
headers = {
    "Content-Type": "application/json",
    "trainer_token": TRAINER_TOKEN
}
payload = {
    "name": "Бульбазавр",
    "photo_id": -1
}

try:
    response = requests.post(create_url, headers=headers, data=json.dumps(payload))
    print(f"Status code: {response.status_code}")
    print(f"Raw response: {response.text}")  # Добавьте эту строку
    response.raise_for_status()
    pokemon_data = response.json()
    pokemon_id = pokemon_data.get("id")
    print("Response:")
    print(json.dumps(response.json(), indent=4, ensure_ascii=False))
    pokemon_id = response.json().get("id")
except Exception as e:
    print(f"Ошибка при создании покемона: {e}")
    pokemon_id = None

# 2. Изменение имени покемона (PUT /pokemons)
if pokemon_id:
    print("\n2. Изменение имени покемона:")
    update_url = f"{BASE_URL}/pokemons"
    payload = {
        "pokemon_id": pokemon_id,
        "name": "Ивизавр",
        "photo_id": 12
    }

    try:
        response = requests.put(update_url, headers=headers, data=json.dumps(payload))
        print(f"Status code: {response.status_code}")
        print("Response:")
        print(json.dumps(response.json(), indent=4, ensure_ascii=False))
    except Exception as e:
        print(f"Ошибка при изменении покемона: {e}")

# 3. Поймать покемона в покебол (POST /trainers/add_pokeball)
if pokemon_id:
    print("\n3. Поймать покемона в покебол:")
    pokeball_url = f"{BASE_URL}/trainers/add_pokeball"
    payload = {
        "pokemon_id": pokemon_id
    }

    try:
        response = requests.post(pokeball_url, headers=headers, data=json.dumps(payload))
        print(f"Status code: {response.status_code}")
        print("Response:")
        print(json.dumps(response.json(), indent=4, ensure_ascii=False))
    except Exception as e:
        print(f"Ошибка при добавлении в покебол: {e}")
else:
    print("\nПропуск добавления в покебол - покемон не был создан")