## simple while loop driven menu that keeps asking the user to choose and action until the press q to quit
orders = list()

def check_order_amount(order_amount):
    try:
        order_amount = float(order_amount)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return
    return order_amount
while True:
    print("1. Add order amount to running list")
    print("2. show all order amounts")
    print("q. Quit")
    choice = input("Enter your choice: ")
    if choice == "q":
        break
    elif choice == "1":
        order_amount = check_order_amount(input("Enter the order amount: "))
        if order_amount:
            orders.append(order_amount)
    elif choice == "2":
        print(orders)
    print("\n")