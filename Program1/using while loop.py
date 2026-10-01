n = int(input("Enter number of subjects: "))
total = 0
i = 1

while i <= n:
    mark = float(input(f"Enter mark {i}: "))
    total += mark
    i += 1

average = total / n

if average >= 90:
    grade = "A+"
elif average >= 75:
    grade = "A"
elif average >= 60:
    grade = "B"
elif average >= 50:
    grade = "C"
else:
    grade = "Fail"

print("Total:", total)
print("Average:", average)
print("Grade:", grade)