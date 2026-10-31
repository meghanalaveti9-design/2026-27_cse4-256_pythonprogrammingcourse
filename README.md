# Case Study 57: Smart Canteen Order and Stock Management

## 1. Problem Statement
Process canteen orders, calculate bills, update stock, reject unavailable quantities, and summarize sales and remaining inventory.

## 2. Objectives
- Display a menu and current stock.
- Process repeated customer orders.
- Prevent orders exceeding available stock and calculate total sales.

## 3. Assumptions
- The menu has tea, sandwich, and juice.
- Initial stock and prices are fixed in the program.
- The user enters item numbers and quantities; 0 ends ordering.

## 4. Algorithm
1. Start with menu, prices, stock, and total sales.
2. Display menu and ask for item number.
3. If item number is 0, stop ordering.
4. Validate item number and quantity.
5. If enough stock exists, calculate bill, reduce stock, and add to sales.
6. Otherwise reject the order.
7. Display total sales and remaining stock.
8. Stop.

## 5. Flowchart
The flowchart below shows the general flow of this program. The validation and processing boxes correspond to the specific steps in the algorithm.

```mermaid
flowchart TD
    A([Start]) --> B[Input data]
    B --> C{Validate input}
    C -->|Invalid| D[Display error]
    D --> Z([End])
    C -->|Valid| E[Process using conditions and loops]
    E --> F[Calculate results]
    F --> G[Display report]
    G --> Z([End])
```

## 6. Pseudocode
```text
START
SET menu, prices, stock, sales = 0
REPEAT
  DISPLAY menu and stock
  INPUT item number
  IF item number = 0: EXIT LOOP
  IF invalid item: DISPLAY error; CONTINUE
  INPUT quantity
  IF quantity <= 0: DISPLAY error
  ELSE IF quantity > stock: REJECT order
  ELSE: bill = price * quantity; stock = stock - quantity; sales = sales + bill
UNTIL item number = 0
DISPLAY sales and remaining stock
STOP
```

## 7. Python Source Code
The complete runnable program is saved in [`program.py`](program.py).

```python
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
```

## 8. Test Cases
- **Input:** Order 2 sandwiches, then finish
  **Expected result:** Bill = ₹80; sandwich stock decreases from 15 to 13; total sales = ₹80.

**Note:** Run the program with the test inputs above and capture the actual console output for the submission screenshots.

## 9. Output Screenshot
Add a screenshot of the program running here after executing `program.py`.

Suggested filename: `output.png`

## 10. Conclusion
The program manages canteen orders, updates stock after valid sales, and reports daily sales.
