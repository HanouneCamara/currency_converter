import requests
import tkinter as tk
from tkinter import messagebox


def get_exchange_rate(base_currency, target_currency):
    try:
        url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
        response = requests.get(url)
        data = response.json()
        return data['rates'][target_currency]
    except Exception as e:
        messagebox.showerror("Erreur", "Impossible de récupérer les taux de change.")
        return None


def convert_currency():
    try:
        amount = float(entry_amount.get())
        base_currency = entry_base_currency.get().upper()
        target_currency = entry_target_currency.get().upper()
        rate = get_exchange_rate(base_currency, target_currency)
        if rate:
            converted_amount = amount * rate
            label_result.config(text=f"{amount} {base_currency} équivaut à {converted_amount:.2f} {target_currency}")
    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer un montant valide.")
        


# Création de la fenêtre principale
root = tk.Tk()
root.title("Convertisseur de devises")

# Création des widgets
label_amount = tk.Label(root, text="Montant :")
label_amount.grid(row=0, column=0, padx=10, pady=10)

entry_amount = tk.Entry(root)
entry_amount.grid(row=0, column=1, padx=10, pady=10)

label_base_currency = tk.Label(root, text="Devise de base (ex: MRU) :")
label_base_currency.grid(row=1, column=0, padx=10, pady=10)

entry_base_currency = tk.Entry(root)
entry_base_currency.grid(row=1, column=1, padx=10, pady=10)

label_target_currency = tk.Label(root, text="Devise cible (ex: EUR) :")
label_target_currency.grid(row=2, column=0, padx=10, pady=10)

entry_target_currency = tk.Entry(root)
entry_target_currency.grid(row=2, column=1, padx=10, pady=10)

button_convert = tk.Button(root, text="Convertir", command=convert_currency)
button_convert.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

label_result = tk.Label(root, text="")
label_result.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Lancement de la boucle principale
root.mainloop()   