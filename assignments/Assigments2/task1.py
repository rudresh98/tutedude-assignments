try:
    order_amount = int(input("Enter the order amount: "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
    exit()

def apply_discount(order_amount):
    tax = 0.05
    if order_amount >= 2000:
        discount = order_amount * 0.15
        final_amount = order_amount - discount
        print("Subtotal: ", final_amount)
        tax_amount = final_amount * tax
        print("Tax amount: ", tax_amount)
        total_amount = final_amount + tax_amount
        print("Total amount: ", total_amount)

    elif order_amount >= 1500 and order_amount < 2000:
        discount = order_amount * 0.10
        final_amount = order_amount - discount
        print("Subtotal: ", final_amount)
        tax_amount = final_amount * tax
        print("Tax amount: ", tax_amount)
        total_amount = final_amount + tax_amount
        print("Total amount: ", total_amount)
    elif order_amount >= 1000 and order_amount < 1500:
        discount = order_amount * 0.07
        final_amount = order_amount - discount
        print("Subtotal: ", final_amount)
        tax_amount = final_amount * tax
        print("Tax amount: ", tax_amount)
        total_amount = final_amount + tax_amount
        print("Total amount: ", total_amount)
    else:
        print("Final amount: ", order_amount)

apply_discount(order_amount)