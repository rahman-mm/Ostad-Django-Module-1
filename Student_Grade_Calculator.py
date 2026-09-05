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
    print(f"Grade: {grade}")

elif 70 <= average_marks <=79:
    grade= "A"
    print(f"Grade: {grade}")

elif 60 <= average_marks <=69:
    grade= "B"
    print(f"Grade: {grade}")

elif 50 <= average_marks <=59:
    grade= "C"
    print(f"Grade: {grade}")

else:
    grade= "F"
    print(f"Grade: {grade}")

