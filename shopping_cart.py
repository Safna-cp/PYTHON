cart = []

while True:
    print("\nMenu:")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. Update Item")
    print("4. View Cart")
    print("5. Search Item")
    print("6. Slice Cart")
    print("7. Sort Cart")
    print("8. Exit")

    choice = input("Choose (1-8): ")

    if choice == "1":
        item = input("Add item: ")
        cart.append(item)
        print("Added:", item)

    elif choice == "2":
        item = input("Remove item: ")
        if item in cart:
            cart.remove(item)
            print("Removed:", item)
        else:
            print("Item not found.")

    elif choice == "3":
        if len(cart) == 0:
            print("Cart is empty.")
        else:
            for i in range(len(cart)):
                print(i, cart[i])
            index = input("Index to update: ")
            if index.isdigit():
                index = int(index)
                if 0 <= index < len(cart):
                    new_item = input("New item: ")
                    cart[index] = new_item
                    print("Updated item at index", index)
                else:
                    print("Invalid index.")
            else:
                print("Enter a number.")

    elif choice == "4":
        if len(cart) == 0:
            print("Cart is empty.")
        else:
            for i in range(len(cart)):
                print(i, cart[i])

    elif choice == "5":
        item = input("Search item: ")
        if item in cart:
            print("Found at index", cart.index(item))
        else:
            print("Not found.")

    elif choice == "6":
        if len(cart) == 0:
            print("Cart is empty.")
        else:
            start = input("Start index: ")
            end = input("End index: ")
            if start.isdigit() and end.isdigit():
                start = int(start)
                end = int(end)
                print(cart[start:end])
            else:
                print("Enter numbers.")

    elif choice == "7":
        cart.sort()
        print("Cart sorted.")

    elif choice == "8":
        print("Bye!")
        break

    else:
        print("Invalid choice.")
