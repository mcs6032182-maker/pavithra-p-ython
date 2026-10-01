n = int(input("Enter number of subjects: "))

marks = [int(input("Enter mark: ")) for i in range(n)]

total = sum(marks)
average = total / n

print("Marks:", marks)
print("Total:", total)
print("Average:", average)

if average >= 90:
    print("Grade: A+")
elif average >= 75:
    print("Grade: A")
elif average >= 60:
    print("Grade: B")
elif average >= 50:
    print("Grade: C")
else:
    print("Grade: Fail")