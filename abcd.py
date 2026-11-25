import os
import pickle
with open("abcd.bin","wb") as a:
    d="hello i am a good man"
    q=pickle.dump(d,a)
    print("done")
with open("abcd.bin","rb") as a:
    d="hello i am a good man"
    q=pickle.load(a)
    print(q)
    
