class User:
    def __init__(self, name, age, gender, password):
        self.name   = name
        self.age    = age
        self.gender = gender
        self.password = password

    def __str__(self):
        return f'{self.name}, {self.age}'