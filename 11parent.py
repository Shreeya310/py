class Person(object):
    def __init__(self,name,idname):
        self.name=name
        self.idname=idname
    def display(self):
        print(self.name)
        print(self.idname)    
class employ(Person):
    def __init__(self,name,idname,income,designation):
        self.income=income
        self.designation=designation
        Person.__init__(self,name,idname)
s=employ('Raman',12345,67890,"CEO")
s.display()        
        