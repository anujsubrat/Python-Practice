class anuj:
    def __init__(self,d,e):
        self.x=d
        self.y=e
    def display(self):
        print("x=",self.x)
        print("y=",self.y)
        
ob=anuj("Anuj Subrat","kriti")
ob.y="Kriti Kushvaha"
print(ob.y)
ob.display()

        
