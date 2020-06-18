
Amazon = {
    "Hello": "Select your address",
    "customer service":"24 hrs",
    "categories": ["laptops", "mobiles", "Best sellers", "pantry"],
    "Hello,Sign in": "Account & Lists"

}

print(Amazon)
print(type(Amazon))
print(len(Amazon))

product1 = {
    "name": "Lenovo ideapad slim",
    "price": 49990,
}

product2 = {
    "name": "HP 14",
    "price": 25490,
}

product3 = {
    "name": "Apple Macbook Air",
    "price": 65500,

}
product4 = {
    "name": "AUES Vivobook",
    "price": 40990,
}
product5 = {
    "name": "DEll Inspiron 3583",
    "price": 58200,
}
product6 = {
    "name": "HP Pavillion x360 ",
    "price": 49197,
}


products = [product1, product2, product3, product4, product5, product6]

Amazon["products"] = products

print(Amazon)