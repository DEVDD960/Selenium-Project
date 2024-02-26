import csv

my_dict = {'a':1, 'b':2,'c':3}

f=csv.DictWriter(open("test.csv", "a"), fieldnames=list(my_dict.keys())) 
f.writerow(my_dict)
   

with open("test.csv", "a") as fs:
    fs.write("2,4,3,2\n")
