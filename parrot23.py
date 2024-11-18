class Parrot:
    species="Bird"
    def __init__(self,name,age):
        self.name=name
        self.age=age
sss=Parrot("sss",45)
yyy=Parrot("yyy",89)   
print("{} is {} years old.".format(sss.name,sss.age))
print("{} is {} years old.".format(yyy.name,yyy.age))

