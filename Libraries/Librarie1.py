import pandas as pd #alias whicwhich is an nick name 
import numpy as np
from matplotlib import pyplot as plt

read_sale_report = pd.read_csv(filepath_or_buffer = r"D:\nisanth figma\PSNL\Python_programming\Libraries\sales_data.csv")

axis_by_row = np.repeat(a=read_sale_report,repeats=2,axis=1)
print(axis_by_row)

table_view = pd.DataFrame(axis_by_row)
print(table_view)

plt.hist(x=read_sale_report.age)
plt.show()