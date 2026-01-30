import pandas as pd

# load csv file
df = pd.read_csv("ecommerce_data.csv")

# preparing data
df["order_date"] = pd.to_datetime(df["order_date"])
df["order_values"] = df["quantity"] * df["price"]

# total revenue
total_revenue = df["order_values"].sum()

# top products by revenue
top_products = (
    df.groupby("product")["order_values"]
    .sum()
    .sort_values(ascending=False)
)

# revenue by category
revenue_by_category = df.groupby("category")["order_values"].sum()

# customer spending 
customer_spending = (
    df.groupby("customer_id")["order_values"]
    .sum()
    .sort_values(ascending=False)
)

print("Total Revenue : ")
print(total_revenue)

print("\nTop Products By Revenue : ")
print(top_products)

print("\nRevenue By Category: ")
print(revenue_by_category)

print("\nCustomer Spending: ")
print(customer_spending)
