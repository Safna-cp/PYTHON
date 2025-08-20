subjects = {"maths", "chemistry" , "english", "history"}
print(subjects)

subjects.add("biology")
print("Updated subject set:", subjects)


for item in subjects:
    print(item)

unique_subject = set(subjects)
print("Unique subjects", unique_subject)

print("total",len(unique_subject))




