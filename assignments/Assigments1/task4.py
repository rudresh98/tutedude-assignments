productsList = [
    {"product": "product1", "category": "Electronics",},
    {"product": "product2", "category": "Clothing", },
    {"product": "product3", "category": "Electronics", },
    {"product": "product4", "category": "Clothing", },
    {"product": "product5", "category": "Electronics", },
    {"product": "product6", "category": "Clothing", }
]
price_dict = {
    "product1": 120,
    "product2": 220,
    "product3": 320,
    "product4": 420,
    "product5": 520,
    "product6": 620
}
productTuple = tuple(productsList)

catalog = [(product["product"], price_dict[product["product"]], product["category"]) for product in productsList]
print(catalog,type(catalog))


## all the products that belongs to the category has the max number of products
max_category = max(set(product["category"] for product in productsList), key=productsList.count)
print(max_category)

    