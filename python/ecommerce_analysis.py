import pandas as pd 
df= pd.read_csv("data/ecommerce_sales_project_dataset.csv")
print(df.head())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

df=df.drop_duplicates()
print("\nAfter removing duplicates:")
print(df.shape)

print("\ndata types:")
print(df.dtypes)
df["Order_Date"]= pd.to_datetime(df["Order_Date"],errors="coerce")
print("\nOrder Date Type:")
print(df["Order_Date"].dtype)
print(df[df.isnull().any(axis=1)])

df.loc[df["City"].isna(),"City"]="Unknown"
df["Payment_Mode"]=df["Payment_Mode"].fillna("Unknown")
df["Product"]=df["Product"].fillna("Unknown")
df["Quantity"]=df["Quantity"].fillna(df["Quantity"].median())
print("\nMissing Values after cleaning:")
print(df.isnull().sum())

print("\nFinal dataset shape:")
print(df.shape)

print("\nTotal Sales:")
print(df["Sales"].sum())

print("\nTotal Profit:")
print(df["Profit"].sum())
average_order_value = df.groupby("Order_ID")["Sales"].sum().mean()
print("\nAverage Order Value:")
print(round(average_order_value,2))

print("\nSales by Category:")
print(df.groupby("Category")["Sales"].sum().sort_values(ascending=False))
print("\nProfit by Category:")
print(df.groupby("Category")["Profit"].sum().sort_values(ascending=False))

print("\nSales by Region:")
print(df.groupby("Region")["Sales"].sum().sort_values(ascending=False))

df["Month"] = df["Order_Date"].dt.to_period("M")
monthly_sales= df.groupby("Month")["Sales"].sum()

print("\nMonthly Sales:")
print(monthly_sales)

payment_sales = df.groupby("Payment_Mode")["Sales"].sum().sort_values(ascending=False)
print("\nSales by payment Mode:")
print(payment_sales)

top_products=(df.groupby("Product")["Sales"].sum().sort_values(ascending=False).head(10))
print("\nTop 10 Products by Sales:")
print(top_products)

total_sales= df["Sales"].sum()
total_profit=df["Profit"].sum()
profit_margin = (total_profit / total_sales)*100
print("\nProfit Margin:")
print(round(profit_margin,2), "%")

import matplotlib.pyplot as plt

category_sales = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)
category_sales.plot(kind="bar")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
