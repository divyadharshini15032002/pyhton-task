class Employee:
    def __init__ (self,name):
        self.__name = name
        self.__salary = 0.0

    def set_salary(self,amount):
        if amount >0:
            self.__salary = amount
        else:
            print("Invalid salary")

    def get_salary(self):
        return self.__salary
    
    def get_name(self):
        return self.__name

emp = Employee("sabith")
emp.set_salary(6800)
print(emp.get_salary())

emp.set_salary(-100)
print(emp.get_name())
