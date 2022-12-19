class a_class():
    def __init__(self, value):
        self.value = value


def change_a_value(a):
    a.value += 1


a = a_class(value=1)
change_a_value(a)

print(a.value)
