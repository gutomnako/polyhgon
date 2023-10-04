# This entrypoint file to be used in development. Start by reading README.md
import budget
from budget import create_spend_chart
from unittest import main

food = budget.Category("Food")
food.deposit(1000.00, "initial deposit")
food.withdraw(100.00, "groceries")
food.withdraw(500.00, "restaurant and more food for dessert")
clothing = budget.Category("Clothing")
clothing.deposit(1000.00, "initial deposit")
food.transfer(50.00, clothing)
clothing.withdraw(400.00, "Clothing")
auto = budget.Category("Auto")
auto.deposit(1000.00, "initial deposit")
auto.withdraw(200.00, "Auto")
auto.transfer(400.00, clothing)
print(food.get_balance())
print(clothing.get_balance())
print(auto.get_balance())

print(food)
print(clothing)
print(auto)

print(create_spend_chart([food, clothing, auto]))
