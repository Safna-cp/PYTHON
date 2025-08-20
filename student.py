student_details={100:"safna",102:"amaya",103:"gokul",104:"anulal"}
print("details of students",student_details)

student_details.update({102:"ashitha"})
print("updated record",student_details)

student_details.pop(104)
print("removed item",student_details)

for item,value in student_details.items():
    print(item,":",value)

if 100 in student_details:
    print("present")
else:
    print("not present")

print("total records",len(student_details))




