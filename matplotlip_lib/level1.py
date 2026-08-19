
import pandas as pd

#step2
mtcars_details = pd.read_csv("mtcars.csv")


#step3
print(mtcars_details.shape)
print(mtcars_details.describe())

#step 3.2
from matplotlib import pyplot as plt

plt.hist(mtcars_details["mpg"])
plt.xlabel("MPG")
plt.ylabel("Frequency")
plt.title("MPF Frequency")
plt.show()