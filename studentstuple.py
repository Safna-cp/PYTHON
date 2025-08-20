students = ("Alice", "Bob", "Charlie", "Diana", "Ethan")
print(students)

name_to_find = "Charlie"
position = students.index(name_to_find)
print(f"The position of {name_to_find} in the tuple is: {position}")

name_to_count = "Alice"
count = students.count(name_to_count)
print(f"{name_to_count} appears {count} times in the tuple.")
