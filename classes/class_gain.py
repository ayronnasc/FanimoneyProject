class Gain:
    def __init__(self, user, name, Type, value, date):
        self.user  = user
        self.name  = name
        self.type  = Type
        self.value = value
        self.date  = date

    def __str__(self):
        return f'Ganho de {self.user}, {self.name}, com valor de {self.value}, {self.type}'

