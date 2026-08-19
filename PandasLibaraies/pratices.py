import pandas as pd

data = {
    'city': ['Chennai', 'Bangalore', 'Chennai', 'Coimbatore', 'Bangalore', 'Coimbatore'],
    'category': ['Electronics', 'Clothing', 'Clothing', 'Electronics', 'Electronics', 'Clothing'],
    'order_amount': [12000, 2500, 1800, 8500, 15000, 3200],
    'delivery_days': [2, 4, 3, 2, 5, 3]
}

df = pd.DataFrame(data)
print(df)


total_order_amount = df.groupby("city")["order_amount"].sum()

print(total_order_amount)

average_delivery_days = df.groupby("category")["delivery_days"].mean()
print(average_delivery_days)

average= df.groupby("category")["order_amount"].agg(['min', 'max', 'mean'])
print(average)

city_cat_sales = df.groupby(['city', 'category'])['order_amount'].sum()
print(city_cat_sales)