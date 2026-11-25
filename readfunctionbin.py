import pickle
f=open("mca.bin","rb")
d=pickle.load(f)
print(d["Name"])
f.close()
