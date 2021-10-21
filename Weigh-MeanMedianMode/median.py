import csv
import pandas as pd
import plotly_express as px
from os import name
with open('SOCR-HeightWeight.csv' , newline="") as f:
   reader = csv.reader(f)
   x = list(reader)
x.pop(0)
n=len(x[2])

x.sort()
if n%2==0:
    median1 = float(x[n//2])
    median2 = float(x[n//2-1])
    median = (median1+median2)/2
else:
    median = x[n//2]
print("Median is " + str(median))
