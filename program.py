menu = ["Tea", "Sandwich", "Juice"]
prices = [10, 40, 25]
stock = [30, 15, 20]
sales = 0

while True:
    print("\nSMART CANTEEN MENU")
    for i in range(len(menu)):
        print(i + 1, menu[i], "- Rs.", prices[i], "| Stock:", stock[i])
    print("0. Finish orders")
    choice = int(input("Choose item number: "))

    if choice == 0:
        break
    if choice < 1 or choice > len(menu):
        print("Invalid item number.")
        continue

    quantity = int(input("Enter quantity: "))
    if quantity <= 0:
        print("Quantity must be positive.")
    elif quantity > stock[choice - 1]:
        print("Not enough stock. Order rejected.")
    else:
        bill = prices[choice - 1] * quantity
        stock[choice - 1] -= quantity
        sales += bill
        print("Order accepted. Bill: Rs.", bill)

print("\nDAILY SUMMARY")
print("Total sales: Rs.", sales)
print("Remaining stock:")
for i in range(len(menu)):
    print(menu[i], ":", stock[i])
