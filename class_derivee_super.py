class Employee:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
class Boss(Employee):
    def __init__(self, name, surname):
        # Sans super
        # Employee.__init__(self, name, surname)
        super().__init__(name, surname)
        self.big_boss = True
boss = Boss(name="John", surname="Smith")
print(boss.name, boss.surname)