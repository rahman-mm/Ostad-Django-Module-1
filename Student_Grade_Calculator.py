name= input("Give me the student name: ")

sub_1_marks= float(input("Input the marks of first subject:"))
sub_2_marks= float(input("Input the marks of second subject:"))
sub_3_marks= float(input("Input the marks of third subject:"))


print(f"Student Name: {name}")

total_marks= sub_1_marks + sub_2_marks + sub_3_marks
print(f"Total Marks: {total_marks}")


average_marks= round(total_marks/3, 2)
print(f"Average: {average_marks}")


if average_marks >= 80:
    grade= "A+"

elif average_marks >=70:
    grade= "A"

elif average_marks >=60:
    grade= "B"

elif average_marks >=50:
    grade= "C"

else:
    grade= "F"

print(f"Grade: {grade}")