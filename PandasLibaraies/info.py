import pandas as pd


emp1= pd.DataFrame({
                  "Name":["Nisanth","Navaneethan","Naveen"],
                  "Age":[23,21,31,] 
                  })

emp=pd.read_csv("employees.csv")

print(emp.describe())# to find the  Median value for salary 61000
#Missing Data Cleaning
print(emp["salary"].fillna(61000))
"""
OutPut:

1     62000.0
2     48000.0
3     51000.0
4     78000.0
5     53000.0
6     60000.0
7     50000.0
8     72000.0
9     65000.0
10    61000.0
11    58000.0
12    61000.0
13    61000.0
14    80000.0
"""

#Multi-condition Filtering

chennai_emp = emp[(emp["department"]=="Engineering")&(emp["city"]=="Chennai")]

print(chennai_emp)
"""
Output

   id          name   department     city  age   salary  years_experience
0   1   Arjun Kumar  Engineering  Chennai   28  55000.0                 3
4   5  Vikram Singh  Engineering  Chennai   35  78000.0                10
"""

