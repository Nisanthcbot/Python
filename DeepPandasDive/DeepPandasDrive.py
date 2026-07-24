#pandas Library Deeep Dive(Data Analyst Tool)
"""
  - DataFrames, Series, Indexing, SElection
  - Data Input/Output
  - Data Cleaning Techniques
  - Handling Missing Data
  - Data Visualization with Matplotlib, seaborn, Plotly

"""

import pandas as pd
"""
We have 2 way to read the data

pd.read_csv(filepath_or_buffer =r"D:\nisanth figma\PSNL\Python_programming\DeepPandasDive\data.tsv.txt",sep="\t")
pd.read_table(filepath_or_buffer=r"D:\nisanth figma\PSNL\Python_programming\DeepPandasDive\data.tsv.txt")

"""
order_details =pd.read_table(filepath_or_buffer=r"D:\nisanth figma\PSNL\Python_programming\DeepPandasDive\data.tsv.txt")
order_details.shape
order_details.isnull().sum() #chain of function

