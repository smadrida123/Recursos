#a) Calculating yearly sales from a CSV file: You need to read a CSV file containing sales data and calculate the total sales for each month. 
#You can use the csv module in Python to read the file, 
#process the data, and store the monthly sales in a suitable data structure.
import pandas as pd

database=pd.read_csv("bestsellers-with-categories.csv",sep=",")
print(database)

d=database.groupby(database["Year"]).agg({"Price":"sum"})
print(d)