import numpy as np
import pandas as pd

# Create sales data
data = {
    "Month": [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June"
    ],

    "Laptop": [10, 15, 12, 18, 20, 25],
    "Mobile": [20, 25, 22, 30, 28, 35],
    "Tablet": [8, 12, 10, 15, 18, 20]
}

# Create DataFrame
df = pd.DataFrame(data)

print("========== MONTHLY SALES DATA ==========")
print(df)


# NumPy calculations
laptop = np.array(df["Laptop"])
mobile = np.array(df["Mobile"])
tablet = np.array(df["Tablet"])


print("\n========== SALES STATISTICS ==========")

print("Laptop Total Sales :", np.sum(laptop))
print("Mobile Total Sales :", np.sum(mobile))
print("Tablet Total Sales :", np.sum(tablet))

print("\nLaptop Average Sales :", np.mean(laptop))
print("Mobile Average Sales :", np.mean(mobile))
print("Tablet Average Sales :", np.mean(tablet))


# Find highest monthly sales
print("\n========== HIGHEST SALES ==========")

print("Highest Laptop Sales :", np.max(laptop))
print("Highest Mobile Sales :", np.max(mobile))
print("Highest Tablet Sales :", np.max(tablet))


# Total sales of all products
df["Total Sales"] = (
    df["Laptop"] +
    df["Mobile"] +
    df["Tablet"]
)

print("\n========== TOTAL MONTHLY SALES ==========")
print(df[["Month", "Total Sales"]])


# Find best month
best_month = df.loc[
    df["Total Sales"].idxmax(),
    "Month"
]

highest_total = df["Total Sales"].max()

print("\nBest Sales Month :", best_month)
print("Sales in that Month :", highest_total)


# Product-wise total
product_totals = {
    "Laptop": np.sum(laptop),
    "Mobile": np.sum(mobile),
    "Tablet": np.sum(tablet)
}

best_product = max(
    product_totals,
    key=product_totals.get
)

print("\n========== PRODUCT ANALYSIS ==========")

for product, total in product_totals.items():
    print(product, ":", total)

print("\nBest Selling Product :", best_product)


# Overall statistics
all_sales = np.array(df["Total Sales"])

print("\n========== OVERALL ANALYSIS ==========")

print("Total Sales :", np.sum(all_sales))
print("Average Monthly Sales :", np.mean(all_sales))
print("Maximum Monthly Sales :", np.max(all_sales))
print("Minimum Monthly Sales :", np.min(all_sales))
print("Standard Deviation :", np.std(all_sales))


# Insights
print("\n========== MEANINGFUL INSIGHTS ==========")

print("1. The best selling product is", best_product)

print("2. The best sales month is", best_month)

print("3. Total sales for all months:",
      np.sum(all_sales))

print("4. Average monthly sales:",
      round(np.mean(all_sales), 2))
