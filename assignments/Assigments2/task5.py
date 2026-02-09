daily = [200,150,0,400,50,-1,300]

final_total = 0

def total_sales(order):
    total = 0
    total += order
    return total
        

for i in daily:
    if i < 0:
        break
    elif i==0:
        continue
    else:
        print(i)
        total_sales_amount = total_sales(i)
        final_total += total_sales_amount
        print("Total sales amount: ", total_sales_amount)

print("Final total sales amount: ", final_total)