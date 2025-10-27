class Person:
    
    def __init__(self,name,country,dob):
        self.name = name
        self.country = country
        self.dob = dob
        
    def age(self):
        today= date.today()
        age=today.year - self.dob.year - ((today.month, today.day)> (self.dob.month,self.dob.day))
        return age
    
    name= input("enter name:")
    country=input("enter country:")
    dob=input("enter dob (yyyy-mm-dd):")
    
    person = 'Person'(name, country,dob)
    
    print(f"\nname: {person.name}")
    print(f"country: {person.counntry}")
    print(f"dob:{person.dob}")
    print(f"age:{person.age}years")
        
