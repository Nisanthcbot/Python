#Dictionary 
"""
 it is an Key : value Pair 
 - 2D
 - Heterogenous 
 - Mutable
 - Indexing & slicing is not possible
 - Don't Create duplicate key, but you can create duplicate value 
 
"""

empty_dic ={} # this is how we create Empty Dictionary 


import pandas as pd


math_student_mark = {"Class 1":[90,45,76,78,98,67],"Class 2":[90,45,76,78,98,67]}
print(pd.DataFrame(math_student_mark))