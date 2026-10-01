import numpy as np
import pandas as pd

# Create sales dataset
data = {
    "Product": [
        "Laptop",
        "Mobile",
        "Tablet",
        "Laptop",
        "Mobile",
        "Tablet",
        "Laptop",
        "Mobile"
    ],

    "Quantity": [
        5, 10, 8, 3, 15, 6, 7, 12
    ],

    "Price": [
        50000, 20000, 15000, 50000,
        20000, 15000, 50000, 20000
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate total sales for each row
df["Total_Sales"] = df["Quantity"] * df["Price"]

print("========== SALES DATA ==========")
print(df)

# NumPy calculations
sales = np.array(df["Total_Sales"])

print("\n========== STATISTICAL ANALYSIS ==========")

print("Total Sales       :", np.sum(sales))
print("Average Sales     :", np.mean(sales))
print("Maximum Sale      :", np.max(sales))
print("Minimum Sale      :", np.min(sales))
print("Standard Deviation:", np.std(sales))


# Product-wise sales
print("\n========== PRODUCT-WISE SALES ==========")

product_sales = df.groupby("Product")["Total_Sales"].sum()

print(product_sales)


# Find best-selling product
best_product = product_sales.idxmax()
best_sales = product_sales.max()

print("\nBest Performing Product:", best_product)
print("Sales Amount           :", best_sales)


# Total quantity sold
total_quantity = np.sum(df["Quantity"])

print("\nTotal Quantity Sold:", total_quantity)


# Average quantity sold
average_quantity = np.mean(df["Quantity"])

print("Average Quantity Sold:", round(average_quantity, 2))


# Meaningful insights
print("\n========== INSIGHTS ==========")

print("1. Total sales are:", np.sum(sales))

print("2. Average transaction value:",
      round(np.mean(sales), 2))

print("3. Highest single transaction:",
      np.max(sales))

print("4. Lowest single transaction:",
      np.min(sales))

print("5. Best performing product:",
      best_product)

print("6. Total number of products sold:",
      total_quantity)