import pickle
f=open("mca.bin","wb")
d={"rollnumber":23,"Name":"Anuj"}
pickle.dump(d,f)
print("done")
f.close()
