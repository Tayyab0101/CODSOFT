from typing import Any


class Author:
    def __init__(self, name, book, edition):
        self.name = name
        self.book = book
        self.edition = edition
        
    def __str__(self):
        return f"{self.book} by {self.name}"
    
    def __int__(self):
        # return f"{self.book} from int method"
        return 12
    
    def __call__(self, *args: Any, **kwds: Any):
        print("this instance is now callable using call method")
    
a1 = Author("Tayyab", "This is life", "1st")
print(int(a1))
print(a1)
print(a1.book)
a1()