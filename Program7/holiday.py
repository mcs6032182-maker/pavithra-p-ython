import numpy as np
import pandas as pd

# Create holiday travel data
data = {
    "Destination": [
        "Goa",
        "Ooty",
        "Manali",
        "Kerala",
        "Jaipur",
        "Mysore"
    ],

    "Visitors": [120, 80, 100, 150, 90, 70],

    "Expense": [15000, 10000, 18000, 14000, 12000, 9000],

    "Rating": [4.5, 4.2, 4.7, 4.8, 4.1, 4.3]
}

# Create DataFrame
df = pd.DataFrame(data)

print("========== HOLIDAY TRAVEL DATA ==========")
print(df)


# Convert columns to NumPy arrays
visitors = np.array(df["Visitors"])
expenses = np.array(df["Expense"])
ratings = np.array(df["Rating"])


# Visitor statistics
print("\n========== VISITOR ANALYSIS ==========")

print("Total Visitors:",
      np.sum(visitors))

print("Average Visitors:",
      np.mean(visitors))

print("Maximum Visitors:",
      np.max(visitors))

print("Minimum Visitors:",
      np.min(visitors))


# Expense statistics
print("\n========== EXPENSE ANALYSIS ==========")

print("Average Holiday Expense:",
      np.mean(expenses))

print("Highest Expense:",
      np.max(expenses))

print("Lowest Expense:",
      np.min(expenses))


# Rating statistics
print("\n========== RATING ANALYSIS ==========")

print("Average Rating:",
      round(np.mean(ratings), 2))

print("Highest Rating:",
      np.max(ratings))

print("Lowest Rating:",
      np.min(ratings))


# Most visited destination
popular = df.loc[df["Visitors"].idxmax()]

print("\n========== MOST VISITED DESTINATION ==========")

print("Destination:",
      popular["Destination"])

print("Visitors:",
      popular["Visitors"])


# Highest rated destination
best_rated = df.loc[df["Rating"].idxmax()]

print("\n========== HIGHEST RATED DESTINATION ==========")

print("Destination:",
      best_rated["Destination"])

print("Rating:",
      best_rated["Rating"])


# Most expensive destination
expensive = df.loc[df["Expense"].idxmax()]

print("\n========== MOST EXPENSIVE DESTINATION ==========")

print("Destination:",
      expensive["Destination"])

print("Expense:",
      expensive["Expense"])


# Budget destinations
print("\n========== BUDGET DESTINATIONS ==========")

budget = df[df["Expense"] < 12000]

print(budget[["Destination", "Expense"]])


# Popular destinations
print("\n========== POPULAR DESTINATIONS ==========")

popular_places = df[df["Visitors"] >= 100]

print(popular_places[["Destination", "Visitors"]])


# Meaningful insights
print("\n========== HOLIDAY INSIGHTS ==========")

print("1. Total visitors:",
      np.sum(visitors))

print("2. Average visitors:",
      round(np.mean(visitors), 2))

print("3. Most visited destination:",
      popular["Destination"])

print("4. Highest rated destination:",
      best_rated["Destination"])

print("5. Most expensive destination:",
      expensive["Destination"])

print("6. Average holiday expense:",
      round(np.mean(expenses), 2))
