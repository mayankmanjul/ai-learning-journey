class Student:
    name = "mayank"
    def __init__(self, name, bases, dict, /, **kwds):
        pass

    def __init__(self, fullname,marks):
        self.name = fullname
        self.marks = marks
        print(self)
        print("Adding new student in repository..")

# Object creation
s1 = Student("Mayank",98)
print(s1.name,s1.marks)
print("Program started")

s2 = Student("Anaya",98)
print(s2.name,s2.marks)
print("Program started")