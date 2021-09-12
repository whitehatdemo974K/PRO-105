import csv 
import math
with open("data.csv",newline="") as f:
    reader=csv.reader(f)
    file_data=list(reader)

data=file_data[0]

def mean(data):
    count=len(data)
    total=0
    for i in data:
        total=total+int(i)
    mean=total/count
    print("This is the Mean",mean)
    return mean

sqr_list=[]
for value in data:
    a=int(value)-mean(data)
    a=a**2
    sqr_list.append(a)

sum=0
for i in sqr_list:
    sum=sum+i

result=sum/(len(data)-1)
std_dev=math.sqrt(result)
print("Std_Dev",std_dev)