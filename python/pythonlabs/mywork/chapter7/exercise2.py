class Person:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return '{} is a {} who is {} years old'.format(self.name, self.gender, self.age)

class Family:

    def __init__(self, parent1, parent2, *children):
        self.parent1 = parent1
        self.parent2 = parent2
        self.children = list(children)

    def add_child(self, child):
        self.children.append(child)

    def __str__(self):
        kid_represent = list()
        kid_represent = [str(i) for i in self.children]
        kid_str = ', '.join(kid_represent)
        fmt = '{} and {}.\nTogether they have {} children: {}'
        return fmt.format(self.parent1, self.parent2, len(self.children), kid_str)
