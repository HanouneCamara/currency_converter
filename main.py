import requests

def get_exchange_rate(base_currency, target_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(url)
    data = response.json()
    return data['rates'][target_currency]

base = "USD"
target = "EUR"
rate = get_exchange_rate(base, target)
print(f"Le taux de change de {base} à {target} est {rate}")