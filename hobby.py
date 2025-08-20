hobby_a = {"Swimming", "Drawing", "Playing"}
hobby_b = {"Swimming", "Drawing", "Singing", "Reading"}

common_hobby = hobby_a.intersection(hobby_b)
print("Common hobby", common_hobby)

all_hobby = hobby_a.union(hobby_b)
print("Common hobby", all_hobby)

common_hobby = hobby_a.symmetric_difference(hobby_b)
print("Common hobby", common_hobby)