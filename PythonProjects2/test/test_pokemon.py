import requests
import pytest

# Конфигурация
BASE_URL = "https://api.pokemonbattle.ru/v2"
TRAINER_ID = "123124"  # Замените на ваш реальный ID тренера
TRAINER_NAME = "ЙЦУКЙЦ"  # Замените на имя вашего тренера

def test_get_trainers_status_code_200():
    """
    Тест проверяет, что GET /trainers возвращает статус 200
    """
    response = requests.get(f"{BASE_URL}/trainers")
    assert response.status_code == 200, (
        f"Ожидался статус 200, но получен {response.status_code}. "
        f"Ответ сервера: {response.text}"
    )

def test_trainer_name_in_response():
    """
    Тест проверяет, что в ответе есть тренер с указанным ID и именем
    """
    # Отправляем запрос с параметром trainer_id
    response = requests.get(
        f"{BASE_URL}/trainers",
        params={"trainer_id": TRAINER_ID}
    )
    
    # Проверяем статус код
    assert response.status_code == 200, (
        f"Запрос вернул статус {response.status_code}. "
        f"Ответ сервера: {response.text}"
    )
    
    # Парсим JSON ответ
    try:
        response_data = response.json()
    except ValueError as e:
        pytest.fail(f"Не удалось распарсить JSON: {e}. Ответ: {response.text}")
    
    # Проверяем структуру ответа
    assert isinstance(response_data, dict), (
        f"Ответ должен быть словарем, получен {type(response_data)}"
    )
    assert "data" in response_data, "В ответе отсутствует поле 'data'"
    
    # Ищем тренера с нужным ID и именем
    trainers = response_data["data"]
    trainer_found = any(
        str(trainer.get("id")) == str(TRAINER_ID) and 
        trainer.get("trainer_name") == TRAINER_NAME
        for trainer in trainers
    )
    
    assert trainer_found, (
        f"Тренер с ID {TRAINER_ID} и именем '{TRAINER_NAME}' не найден. "
        f"Полный ответ: {response_data}"
    )