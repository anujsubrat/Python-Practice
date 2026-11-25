class a:
    def __init__(self):
        self.x=100
class b(a):
    pass
class c(b):
    pass

ob=c()
print(ob.x)
