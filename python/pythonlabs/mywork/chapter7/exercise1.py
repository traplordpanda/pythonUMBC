class Person:
    
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def __str__(self):
        fmt = '{}'
        return '{} is a {} who is {} years old'.format(self.name, self.gender, self.age)