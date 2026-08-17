import pandas as pd

emp=pd.read_csv(filepath_or_buffer="employees.csv")

#Find out the Deparment in the company 
emp.nunique()# it will find number of Unique 

print(emp["department"].unique())

"""
 nunique() is used to find the number of unique in the dataframe
 this helps to find out the Department in the company bu unsing unique() function 

"""

#Top Employee Count in deparment with Salary 

print(emp.groupby(by="department")["salary"].sum()) #while using groupby function we have to use 2 column in this we have to pass by ="Column Name" and [''] and then if we needs to short the colum by value we have to use short_value() function 
