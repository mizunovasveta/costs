import requests
from .models import Currency


def load_currencies():
    API_KEY = '01c8b1ebdcc44d3e89762c1f853c6e0b'
    URL = f'https://openexchangerates.org/api/currencies.json?app_id={API_KEY}'
    response = requests.get(URL)
    if response.status_code == 200:
        currencies = response.json()
        Currency.objects.all().delete()
        for code in currencies:
            Currency.objects.create(name=code)
        print("Валюты успешно загружены и сохранены в базу данных.")
    else:
        print(f"Ошибка при получении данных: статус {response.status_code}")
