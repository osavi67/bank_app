from Bank.operations import (
    add_expense,
    add_income,
    calculate_difference,
)
from Bank.wallets import get_wallets


wallets = get_wallets()

balance = 1000

balance = add_income(balance, 500)
balance = add_expense(balance, 200)
result = calculate_difference(1500, 700)

print(result)
print("Кошельки:", wallets)
print(f"Баланс {wallets[0]}:", balance)
