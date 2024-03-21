from os import name


class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def introduce(self):
        return(f'My name is: {self.name}, I am {self.age} years old, I am a {self.gender} ')
    

first_person = Person('Bewaj', 31, 'male')
second_person = Person('Ruthey', 28, 'female')

print(first_person.introduce())
print(second_person.introduce())
        