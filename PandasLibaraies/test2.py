import pandas as pd


df = pd.read_csv("employees.csv")

print(df.iloc[1:5,1:3])

Average_salary = df["salary"].mean()
print(df["salary"].fillna(Average_salary))
print(df.groupby("department")["name"].count())

print(df.sort_values("salary",ascending=False).head(2))

print(df.isnull().sum())
print(df[df.isnull()].sum())

remove_null =df.dropna(subset=["salary"])#to remove Null value 
print(remove_null)

print(df.drop("salary",axis=1))#remove Column

print(df.drop_duplicates("years_experience"))
df["job status"] = True #new Column 
print(df)