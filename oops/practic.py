class Dog:
    def __init__(self,name):
        self.name=name 
    def display_name(self):
        print(f"Dog's name is {self.name}")
    
class Labrador(Dog):
    def sound(self):
        print("labrador woofs")

class GuideDog(Labrador):
    def guide(self):
        print(f"{self.name} guides the way")

class Friendly:
    def greet(self):
        print("Friendly!")

class GoldenRetriever(Dog,Friendly):
    def sound(self):
        print("Golden retriever barks")


lab=Labrador("BUDDY")
lab.display_name()
lab.sound()

guide_dog=GuideDog("GUIDE")
guide_dog.guide()
guide_dog.display_name()

retriev=GoldenRetriever("RETRIEVER")
retriev.display_name()
retriev.sound()
retriev.greet()