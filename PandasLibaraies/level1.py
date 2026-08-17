import pandas as pd

emp=pd.read_csv(filepath_or_buffer="employees.csv")




# Terminology Alert 
"""
  # Rows - Oberservation/records
  # Column - Features/ Parameters
   
"""
#
emp.shape

#Null value 

print(emp.isnull().sum())# chain of function(), chain of Commands



print(emp.describe(include='all'))



"""
Level - 1 in Analysis 

1) perform Initial Analysis by using shape Attribute (give no of row and colum)
2) next we have to check whether there is Null value or not using isnull() function 
3) we have to find the data type in every column by using dtype attribute
4) and finaly we have to use describe() to get insites 

"""
