# Pandas Library
# Data processing and analysis 

import pandas as pd
data = pd.read_csv('diabetes.csv')
print(data.head())

#data type of the above dataframe
type(data)

#rename a coloumn names
data.rename(columns={"Pregnancies": 'Pragnent Womens', "Glucose": 'Glucose Data'})
data

#first five coloumn of the dataset
data.tail()

#shape of the dataset
data.shape

#shows how many coloumns are there in the dataset
data.columns
#full information about the data set
data.info()

#to check the number of missing values in the dataframe
data.isnull().sum()

 # count the number of values based on the labels
data.value_counts('Glucose') 

# Here we will import two modules 
import random
import numpy as np

#How to create a dataframe with a random values
random_df = pd.DataFrame(np.random.rand(10, 50))
random_df.head()

# Pandas Series 
a = [1, 7, 2]
myvar = pd.Series(a, index = ["x", "y", "z"])

myvar = pd.Series(myvar)

print(myvar)

#labels in the Series
(myvar[2])

# Pandas Series from dictionary 
calaroies = {"Day1": "350", "Day2": "370", "Day3": "380"}
d_data = pd.Series(calaroies)
d_data

#Create a DataFrame: Dataframe is a two dimensions data structure, like an array or a table with rows and coloumns.
my_data = {
    "Names": ["Salman", "Sohail", "Naeem", "Shahid", "Anees", "Sajad"],
    "Class": ["CS_5th", "CS_5th", "CS_5th", "CS_5th", "CS_5th", "CS_5th"],
    "Marks": [89, 87, 90, 98, 78, 87],
    "Location": ["Dir Lower", "Timargara", "Khall", "Bajawar", "Swat", "Kabal"]
    
}
pd.DataFrame(my_data)
