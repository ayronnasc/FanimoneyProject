class Outgoing:
    def __init__(self, user, name, Type, installments, value, date):
        self.user = user
        self.name = name
        self.type = Type
        self.installments = installments
        self.value = value
        self.date = date

    def __str__(self):
        return f'Gasto de {self.user}, {self.name}, no valor de {self.value}, {self.type}'

