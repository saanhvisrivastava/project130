import csv
import pandas as pd 
df=pd.read_csv('sorted.csv')
#print(df)

del df['luminosity']

axis='columns'
df.to_csv('final.csv')
print(df)