import pandas as pd

order_details=pd.read_table(filepath_or_buffer="data.tsv.txt")

print(order_details.groupby("item_name")["quantity"].sum().sort_values(ascending=False).head())

order_details["item_price"] = order_details["item_price"].str.replace("$","").astype(float)

print(order_details.groupby("item_name")["item_price"].sum().sort_values(ascending=False).head())
print(order_details.groupby("item_name")["item_price"])

order_details.to_csv("New_data.csv",index=False)