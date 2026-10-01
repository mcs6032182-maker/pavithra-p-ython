import numpy as np
import pandas as pd

# Create student data
data = {
    "Name": ["pavi", "Priya", "anu", "Anitha", "vino"],
    "Python": [85, 78, 92, 67, 88],
    "Java": [80, 85, 89, 72, 90],
    "Database": [75, 90, 95, 65, 85]
}

# Create DataFrame
df = pd.DataFrame(data)

print("========== STUDENT MARKS ==========")
print(df)


# Convert marks into NumPy arrays
python_marks = np.array(df["Python"])
java_marks = np.array(df["Java"])
database_marks = np.array(df["Database"])


# Calculate total marks
df["Total"] = (
    df["Python"] +
    df["Java"] +
    df["Database"]
)


# Calculate average
df["Average"] = df["Total"] / 3


print("\n========== STUDENT RESULT ==========")
print(df)


# NumPy statistics
print("\n========== STATISTICS ==========")

print("Highest Python Mark :", np.max(python_marks))
print("Lowest Python Mark  :", np.min(python_marks))
print("Average Python Mark :", np.mean(python_marks))

print("Highest Java Mark   :", np.max(java_marks))
print("Lowest Java Mark    :", np.min(java_marks))
print("Average Java Mark   :", np.mean(java_marks))

print("Highest Database Mark :", np.max(database_marks))
print("Lowest Database Mark  :", np.min(database_marks))
print("Average Database Mark :", np.mean(database_marks))


# Find top student
top_student = df.loc[df["Total"].idxmax()]

print("\n========== TOP STUDENT ==========")
print("Name    :", top_student["Name"])
print("Total   :", top_student["Total"])
print("Average :", round(top_student["Average"], 2))


# Find class average
class_average = np.mean(df["Average"])

print("\nClass Average:", round(class_average, 2))


# Pass or Fail
def result(average):
    if average >= 40:
        return "Pass"
    else:
        return "Fail"


df["Result"] = df["Average"].apply(result)

print("\n========== FINAL RESULT ==========")
print(df[["Name", "Total", "Average", "Result"]])


# Insights
print("\n========== INSIGHTS ==========")

print("1. Number of students:", len(df))

print("2. Class average:",
      round(class_average, 2))

print("3. Top student:",
      top_student["Name"])

print("4. Highest total marks:",
      top_student["Total"])

print("5. Highest Python mark:",
      np.max(python_marks))

print("6. Highest Java mark:",
      np.max(java_marks))

print("7. Highest Database mark:",
      np.max(database_marks))
