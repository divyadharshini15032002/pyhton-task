class Student:
    def __init__(self,name):
        self.__name = name
        self. __grades = []

    def add_grade(self,grade):
        if isinstance(grade,(int, float)) and 0 <= grade <= 100:
            self.__grades.append(grade)
        else:
            print("Ivalid grade. please enter a number between 0 and 100.")

    def get_average (self):
        if len(self.__grades) == 0:
            return 0
        return sum(self.__grades)/ len(self.__grades)

    def get_name(self):
        return self.__name
    
student=Student("Alice")
student.add_grade(85)
student.add_grade(90)

print(student.get_name())  
print(student.get_average())
