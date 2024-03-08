import requests
from bs4 import BeautifulSoup

class CurrencyConverter:
    def __init__(self):
        self.base_url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=USD&json"
        self.usd_rate = self.get_usd_rate()

    def get_usd_rate(self):
        response = requests.get(self.base_url)
        if response.status_code == 200:
            data = response.json()
            for currency in data:
                if currency["cc"] == "USD":
                    return currency["rate"]
        return None

    def convert_to_usd(self, amount):
        if self.usd_rate:
            usd_amount = amount / self.usd_rate
            return usd_amount
        else:
            return None

if __name__ == "__main__":
    converter = CurrencyConverter()
    amount = float(input("Введіть суму грошей в гривнях "))
    usd_amount = converter.convert_to_usd(amount)
    if usd_amount is not None:
        print(f"{amount} грн = {usd_amount} USD")
    else:
        print("Неможливо конвертувати цю валюту.")
