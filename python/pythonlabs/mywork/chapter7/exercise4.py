class Worker:

    def __init__(self, name, salary, years_worked):
        self.name = name
        self.salary = salary
        self.years_worked = years_worked

    def pension(self):
        return self.years_worked * .10 * self.salary

class Manager(Worker):

    def __init__(self, name, salary, years_worked):
        super().__init__(name, salary, years_worked)

    def pension(self):
        return self.years_worked * .20 * self.salary

class Executive(Worker):

    def __init__(self, name, salary, years_worked):
        super().__init__(name, salary, years_worked)

    def pension(self):
        return self.years_worked * .30 * self.salary
