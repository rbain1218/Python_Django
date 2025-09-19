class student :
    def __init__ (self, name, marks1, marks2, marks3) :
        self.name=name
        self.marks1=marks1
        self.marks2=marks2
        self.marks3=marks3
        

    def average(self):
        return (self.marks1 + self.marks2 + self.marks3)/3

s1=student("Rahul", 85, 90, 88)
s2=student("Rahul2", 92, 81, 79)

print(s1.name)
print(s1.average())
print(s2.name)
print(s2.average())



        
