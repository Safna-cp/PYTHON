days_of_week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print(days_of_week)

first_three_days = days_of_week[:3]
print(first_three_days)

weekend_days = days_of_week[-2:]
print(weekend_days)

if "Friday" in days_of_week:
    print("Friday exists in the tuple.")
else:
    print("Friday does not exist in the tuple.")
