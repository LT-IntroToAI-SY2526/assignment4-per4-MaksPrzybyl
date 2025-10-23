# object oriented programming

# (define-struct dog [fur_color name age favorite_food])

class Dog:
    "Simple class to learn concepts"
    
       
    def __init__(self, breed, fur_color, name, age):
        self.breed = breed
        self.fur_color = fur_color
        self.name = name
        self.age = age


maks_dog = Dog("border_collie","black_white","Juno","9")



def __str__ (self):
    return f"{self.name} is a {self.age} year old {self.fur_color} {self.breed}" 
print(maks_dog)