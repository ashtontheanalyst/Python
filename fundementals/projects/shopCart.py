# Mirrors a shopping cart and prices, practice with lists

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit): ")

    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of {food.lower()}: $"))
        foods.append(food)
        prices.append(price)

print("-------- YOUR CART --------")

for i in range(len(foods)):
    print(f"{foods[i].lower()} costs ${prices[i]:.2f}")

for price in prices:
    total += price

print(f"So your total is ${total:.2f}")
print("---------------------------")