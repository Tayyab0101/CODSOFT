import gc  # Import the gc module for garbage collection

# Define a class representing a Person
class Person:
    def __init__(self, name):
        self.name = name
        print(f"{self.name} created.")

    def __del__(self):
        print(f"{self.name} deleted.")

# Create instances of the Person class
person1 = Person("Alice")
person2 = Person("Bob")

# Create a circular reference
person1.friend = person2
person2.friend = person1

# Delete references to the Person instances
del person1
del person2

# Force garbage collection
print("Garbage collection...")
gc.collect()