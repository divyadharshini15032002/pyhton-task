class country:
    def __init__(self,name):
        self.name =name
    def capital(self):
        print("Each country has its own capital city.")
    def language(self):
        print("Each country has its own official language.")
print()
class india(country):
    def __init__(self):
        super().__init__("india")
    def capital(self):
        print(f"The capital of {self.name} is new delhi.")
    def language(self):
        print(f"The official language of {self.name} is hindi.")
        print()
        
class USA(country):
    def __init__(self):
        super().__init__("USA")
    def capital(self):
        print(f"The capital of {self.name}is washinton,D.C.")
    def language(self):
        print(f"The official language of {self.name} is english.")
        print()
        
class UK(country):
    def __init__(self):
        super().__init__("united kingdom")
    def capital(self):
        print(f"The capital of {self.name} longdan.")
    def language(self):
        print(f"The official language of {self.name} is english.")

india = india()
usa = USA()
uk = UK()
print("country name:",india.name)
india.capital()
india.language()

print("country name:",usa.name)
usa.capital()
usa.language()

print("country name:",uk.name)
uk.capital()
uk.language()
                

        
