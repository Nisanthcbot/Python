import pandas as pd

order_details=pd.read_table(filepath_or_buffer="data.tsv.txt")

print(order_details.isnull().sum()) # there is 1246 null data in choice Description

print(order_details.describe(include='all')) #if we not include all inside the describe function it only take in int value not str,

print(order_details.nunique())

# top 5 item 
print(order_details.groupby("item_name")["quantity"].sum()) # this is helps to group the column by using groupby() function 

print(order_details.groupby("item_name")["quantity"].sum().sort_values()) # by addsort_values() can u arange those 1 by 1 from bottom to top 1-100

print(order_details.groupby("item_name")["quantity"].sum().sort_values(ascending=False)) #by giving ascending = Flase it will give from top to bottom 100 - 1

print(order_details.groupby("item_name")["quantity"].sum().sort_values(ascending=False).head()) #bu giving #head() it return top 5 only by passing the No of value we want in the (10) it retun top 10 



#least 5 selling items 
print(order_details.groupby("item_name")["quantity"].sum().sort_values().head())

order_details["item_price"] = order_details["item_price"].str.replace("$","").astype(float)
print(order_details)
print(order_details.isnull().sum())