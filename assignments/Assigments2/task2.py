orders = [1200,2500,800,1750,3000]

ordersWithDiscount = []
def apply_discount(order_amount):
    tax = 0.05
    if order_amount >= 2000:
        discount = order_amount * 0.15
        final_amount = order_amount - discount
        print("Subtotal: ", final_amount)
        tax_amount = final_amount * tax
        print("Tax amount: ", tax_amount)
        total_amount = final_amount + tax_amount
        print(order_amount, "Total amount: ", total_amount)
        ordersWithDiscount.append(order_amount)

    elif order_amount >= 1500 and order_amount < 2000:
        print("order amount is ", order_amount)
        discount = order_amount * 0.10
        final_amount = order_amount - discount
        print("Subtotal: ", final_amount)
        tax_amount = final_amount * tax
        print("Tax amount: ", tax_amount)
        total_amount = final_amount + tax_amount
        print( "Total amount: ", total_amount)
        ordersWithDiscount.append(order_amount)
    elif order_amount >= 1000 and order_amount < 1500:
        print("order amount is ", order_amount)
        discount = order_amount * 0.07
        final_amount = order_amount - discount
        print("Subtotal: ", final_amount)
        tax_amount = final_amount * tax
        print("Tax amount: ", tax_amount)
        total_amount = final_amount + tax_amount
        print( "Total amount: ", total_amount)
        ordersWithDiscount.append(order_amount)
    else:
        print("order amount is ", order_amount)
        print(order_amount, "Final amount: ", order_amount)
    print("\n")


def checkOrderInput(order_amount):
    try:
        order_amount = float(order_amount)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return
    apply_discount(order_amount)

for order in orders:
    checkOrderInput(order)

print("Orders with discount: ", ordersWithDiscount)