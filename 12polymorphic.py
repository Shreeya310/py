class CAT:
    def __init__(self,name,age):
        self.age=age
        self.name=name
    def info(self):
        print(f"HELLO! I AM {self.name}. I AM {self.age} YEARS OLD.")    
    def make_sound(self):
        print("MEOWWW") 
class DOG:
    def __init__(self,name,age):
        self.age=age
        self.name=name
    def info(self):
        print(f"HELLO! I AM {self.name}.I AM {self.age} YEARS OLD.")    
    def make_sound(self):
        print("BARKKK")            

cat1=CAT("BIRMAN",1.5)
dog1=DOG("SIBERIAN HUSKY",5)
for animal in(cat1,dog1):
    animal.make_sound()
    animal.info()
