productsList = [
    {"product": "product1", "category": "Electronics", "price": 120},
    {"product": "product2", "category": "Clothing", "price": 220},
    {"product": "product3", "category": "Electronics", "price": 320},
    {"product": "product4", "category": "Clothing", "price": 420},
    {"product": "product5", "category": "Electronics", "price": 520},
    {"product": "product6", "category": "Clothing", "price": 620}
]

## set of categories

categories_set = {productsList["category"] for productsList in productsList}
print(categories_set)

## add new category

categories_set.add("Books")
print(categories_set)

## add Electronics again

categories_set.add("Electronics")
print(categories_set)

print("Electronics" in categories_set)