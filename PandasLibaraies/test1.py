import pandas as pd

order_details=pd.read_table(filepath_or_buffer="data.tsv.txt")


print(order_details.info()) #this function show the column ,

#Output
"""
RangeIndex: 4622 entries, 0 to 4621
Data columns (total 5 columns):
 #   Column              Non-Null Count  Dtype
---  ------              --------------  -----
 0   order_id            4622 non-null   int64
 1   quantity            4622 non-null   int64
 2   item_name           4622 non-null   str  
 3   choice_description  3376 non-null   str  
 4   item_price          4622 non-null   str  
dtypes: int64(2), str(3)
memory usage: 180.7 KB
None

"""

print(order_details.shape)

#Output
"""
(4622, 5)
"""

print(order_details.dropna())


quantity= order_details[order_details["quantity"] >=2 ]

print(quantity)

outer_loop = order_details[(order_details["quantity"] >=2) & (order_details["item_name"] =="Chicken Bowl")]
print(outer_loop)

outer_loop["quantity_>2"] = outer_loop["quantity"] >=2

print(outer_loop)