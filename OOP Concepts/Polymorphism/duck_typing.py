class Dog:
    def swim(self):
        print("I'm a dog and I can swim")
    
    def display(self):
        print("Display from Dog class")
        
    def bark(self):
        print("I am a dog and I bark")
        
class Owl:
    def swim(self):
        print("I am an owl and I don't swim")
        
    def bark(self):
        print("I am an owl and I don't bark")
        
def display(obj):
    obj.swim()
    obj.bark()

  
dog1 = Dog()
owl1 = Owl()
dog1.display()
display(owl1)

