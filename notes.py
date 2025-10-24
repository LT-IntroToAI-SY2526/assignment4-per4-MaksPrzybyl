# object oriented programming

# (define-struct dog [fur_color name age favorite_food])

class Dog:
    "Simple class to learn concepts"
    
       
    def __init__(self, breed, fur_color, name, age):
        self.breed = breed
        self.fur_color = fur_color
        self.name = name
        self.age = age
    def __str__ (self):
        return f"{self.name} is a {self.age} year old {self.fur_color} {self.breed}"
    def bark(self):
        return f"{self.name} says: Woof, Woof!!"
    def birthday(self):
        self.age += 1
        print(f"{self.name} is celebrating their {self.age} birthday")
    def paint_dog(self, new_color):
        old_color=self.fur_color
        self.fur_color=new_color
        print(f"{self.name} changed their fur color from {old_color} to {new_color}.")


if __name__ == "__main__":
    maks_dog = Dog("border_collie","black and white","Juno",9)
    default_dog = Dog("mutt","black","no name",1)
    



 
    print(maks_dog)
    print(default_dog)
    maks_dog.bark()
    maks_dog.birthday()
    maks_dog.paint_dog("orange")