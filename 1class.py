class student:
    grade=9
    name="Shreeya"
    print("Hello,I am a student of grade",grade)

    def introduction(self):
        print("Hello,I am a student")
    def details(self):
        print("My name is",self.name)
        print("I am in grade",self.grade)    

vs=student()
vs.introduction()
vs.details()