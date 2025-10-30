class birds:
    def __init__(self,name):
        self.name = name
    def sound(self):
        print("this bird makes a sound:")

class parrot(birds):
    def __init__(self):
        super().__init__("parrot")

    def sound(self):
        print(f"{self.name} says: squawk! hello!")

class sparrow(birds):
    def __init__(self):
        super().__init__("sparrow")
    def sound(self):
        print(f"{self.name}says: chirp chirp!")

bird1 = parrot()
bird2 = sparrow()

print("Bird 1 name:",bird1.name)
bird1.sound()

print("Bird 2 name:",bird2.name)
bird2.sound()
        
