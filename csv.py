import csv
with open("c.csv","w",newline="")as a:
    s=csv.writer(a)
    s.writerow(["hello","anuj"])
    print("done")
 
