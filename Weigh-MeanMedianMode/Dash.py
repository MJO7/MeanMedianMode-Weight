import csv
from os import name
from collections import Counter

x=0
xkg = 0
with open('SOCR-HeightWeight.csv' , newline="") as f:
   reader = csv.reader(f)
   file_data = list(reader)
file_data.pop(0)
new_data=[]
for i in range (len(file_data)):
    n_num = file_data[i][2]
    new_data.append(n_num)

data = Counter(new_data)
mode_data_for_range = {
    "100-110":0,
    "110-120":0,
    "120-130":0
}
for height , occurence in data.items():
    if 100<float(height)<110:
        mode_data_for_range["100-110"]+=occurence
    if 110<float(height)<120:
        mode_data_for_range["110-120"]+=occurence
    if 120<float(height)<130:
        mode_data_for_range["120-130"]+=occurence
mode_range , mode_occurence=0,0
for range , occurence in mode_data_for_range.items():
    if occurence>mode_occurence:
        mode_range, mode_occurence = [int(range.split("-")[0]),int(range.split("-")[1])], occurence
mode = float((mode_range[0]+mode_range[1])/2)
n = len(new_data)
new_data.sort()
if n%2==0:
    median1 = float(new_data[n//2])
    median2 = float(new_data[n//2-1])
    median = (median1+median2)/2
else:
    median = new_data[n//2]
totalWeight = 0
totalNum = (len(file_data))
for i in file_data:
    totalWeight+=float(i[2])
def mean():
   x = totalWeight/totalNum
   xkg = x/2.2046
   print("")
   print("MEAN")
   print("The average weight is "+str(x)+" pounds")
   print("OR")
   print("The average weight is "+str(xkg)+" kilograms")
def media():
    medkg = 127.4271/2.2046
    print("")
    print("MEDIAN")
    print("The median is " + str(median)+" pounds")
    print("OR")
    print("The median is 57.8 kilograms")
    # 127.4271 IS THE MEDIAN IN POUNDS. 127.4271/2.2046 IS 57.8 KILOGRAMS
def mod():
   print("")
   print("MODE")
   print(f"Mode is {mode:2f}")

mean()
media()
mod()