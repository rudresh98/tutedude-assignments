price_dict = {
    "product1": 120,
    "product2": 220,
    "product3": 320,
    "product4": 420,
    "product5": 520,
    "product6": 620
}

## add new product

price_dict["product7"] = 720
print(price_dict)

## update the price of product1

price_dict["product1"] = 333
print(price_dict)

## remove the product1

price_dict.pop("product1")
print(price_dict)


## average price
average_price = sum(price_dict.values()) / len(price_dict)
print(average_price)

## max price
max_price = max(price_dict.values())
print(max_price)

## min price
min_price = min(price_dict.values())
print(min_price)
