import requests

def get_exchange_rate(base_currency, target_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(url)
    data = response.json()
    return data['rates'][target_currency]


def main():
    amount = float(input("Entrez le montant à convertir : "))
    base_currency = input("Entrez la devise de base (ex: EUR) : ").upper()
    target_currency = input("Entrez la devise cible (ex: MRU) : ").upper()
    rate = get_exchange_rate(base_currency, target_currency)
    converted_amount = amount * rate
    print(f"{amount} {base_currency} équivaut à {converted_amount:.2f} {target_currency}")

if __name__ == "__main__":
    main()