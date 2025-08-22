
fruits = [
    {"name": "apple", "price": 2.5, "quantity": 4},
    {"name": "banana", "price": 1.2, "quantity": 10},
    {"name": "orange", "price": 3.0, "quantity": 3}
]

while True:
    name = input("Enter fruit name (or 'stop' to finish): ")
    if name.lower() == 'stop':
        break
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))
    fruits.append({"name": name, "price": price, "quantity": quantity})

print(fruits)
