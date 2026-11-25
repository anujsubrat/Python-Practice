import csv
a=open("c.csv","w",newline="")
s=csv.writer(a)
s.writerow(["hello","anuj"])
print("done")
a.close()
 
