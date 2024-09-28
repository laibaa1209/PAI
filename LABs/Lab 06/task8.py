import pandas as pd


products_df = pd.read_csv("products.csv")
orders_df = pd.read_csv("orders.csv")

print("First 5 rows of Product DataFrame:\n", products_df.head(5))
print("Last 10 rows of Product DataFrame:\n", products_df.tail(10))
print("First 5 rows of Orders DataFrame:\n", orders_df.head(5))
print("Last 10 rows of Orders DataFrame:\n", orders_df.tail(10))


orders_df = orders_df.merge(products_df[['ProductID', 'Price']], on='ProductID', how='left')
orders_df['TotalPrice'] = orders_df['Quantity'] * orders_df['Price']
total_revenue = orders_df['TotalPrice'].sum()
print(f"\nTotal Revenue Generated from all Orders: ${total_revenue:.2f}")

best_selling_products = orders_df.groupby('ProductID').agg({'Quantity': 'sum'}).nlargest(5, 'Quantity')
low_selling_products = orders_df.groupby('ProductID').agg({'Quantity': 'sum'}).nsmallest(5, 'Quantity')

print("\nTop 5 Best-Selling Products:\n", best_selling_products)
print("\nTop 5 Low-Selling Products:\n", low_selling_products)

top_product_ids = best_selling_products.index
top_categories = products_df[products_df['ProductID'].isin(top_product_ids)]['Category']
most_common_category = top_categories.mode()[0]
print(f"\nMost Common Product Category Among the Top 5 Best-Selling Products: {most_common_category}")

average_price_per_category = products_df.groupby('Category')['Price'].mean()
print("\nAverage Price of Products in Each Category:\n", average_price_per_category)

orders_df['OrderDate'] = pd.to_datetime(orders_df['OrderDate'], format='%m-%d-%Y')

daily_revenue = orders_df.groupby(orders_df['OrderDate'].dt.date)['TotalPrice'].sum()
monthly_revenue = orders_df.groupby(orders_df['OrderDate'].dt.to_period('M'))['TotalPrice'].sum()
yearly_revenue = orders_df.groupby(orders_df['OrderDate'].dt.year)['TotalPrice'].sum()

highest_daily_revenue = daily_revenue.idxmax(), daily_revenue.max()
highest_monthly_revenue = monthly_revenue.idxmax(), monthly_revenue.max()
highest_yearly_revenue = yearly_revenue.idxmax(), yearly_revenue.max()

print(f"\nDay with Highest Total Revenue: {highest_daily_revenue[0]} with Revenue: ${highest_daily_revenue[1]:.2f}")
print(f"Month with Highest Total Revenue: {highest_monthly_revenue[0]} with Revenue: ${highest_monthly_revenue[1]:.2f}")
print(f"Year with Highest Total Revenue: {highest_yearly_revenue[0]} with Revenue: ${highest_yearly_revenue[1]:.2f}")

monthly_revenue_df = monthly_revenue.reset_index(name='Total Revenue')
monthly_revenue_df.columns = ['Month', 'Total Revenue']

print("\nTotal Revenue for Each Month:\n", monthly_revenue_df)

print("\nChecking for null values in Products DataFrame:\n", products_df.isnull().sum())
print("\nChecking for null values in Orders DataFrame:\n", orders_df.isnull().sum())

products_df = products_df.dropna()
orders_df = orders_df.dropna()

products_df['Price'] = pd.to_numeric(products_df['Price'], errors='coerce')
orders_df['Quantity'] = pd.to_numeric(orders_df['Quantity'], errors='coerce')

products_df = products_df.dropna()
orders_df = orders_df.dropna()

print("\nData cleaned. Null values removed.")
