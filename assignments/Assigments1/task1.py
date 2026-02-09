productsList= ["product1", "product2", "product3","product4","product5","product6"]
sample_products = ("iphon2",2222,"Electronics")

print("before",sample_products)


## second product 
print(productsList[1])

## last product
print(productsList[-1])

## append two products
productsList.append("product7")
productsList.append("product8")

print(productsList)

## converting tuple to list and back to tuple
sample_products_list = list(sample_products)
sample_products_list[1] = 120
sample_products = tuple(sample_products_list)
print("after",sample_products)
    