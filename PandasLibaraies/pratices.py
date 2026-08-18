import pandas as pd

data = {
    'name': ['Anu', 'Bala', 'Charan', 'Divya', 'Ezhil'],
    'subject': ['Maths', 'Science', 'Maths', 'Science', 'Maths'],
    'score': [85, 72, 90, 68, 95],
    'city': ['Chennai', 'Madurai', 'Chennai', 'Salem', 'Madurai']
}

df = pd.DataFrame(data)
print(df)

math = df[df["subject"]=="Maths"]
print(math)

average = df.groupby("subject")["score"].mean()
print(average)

count = df.groupby("city")["name"].count()
print(count)

count1= df["city"].value_counts()
print(count1)

df["passed"] =df['score'] >= 75

print(df)