fruits = ["Apple", "Banana", "Orange", "Mango", "Pineapple", "Strawberry", "Blueberry", "Kiwi", "Grape", "Watermelon"]
print(fruits)

user_input = input("Enter the name of a fruit: ").strip().capitalize()

if user_input in fruits:
    print(f"{user_input} is in the fruit list!")
else:
    print(f"{user_input} is not in the fruit list.")

