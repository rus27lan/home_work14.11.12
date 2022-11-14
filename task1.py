class Discr:

    def __get__(self, instance, owner):
        return instance.__dict__[self.my_attr]

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Только положительное значение")
        instance.__dict__[self.my_attr] = value

    def __delete__(self, instance):
        del instance.__dict__[self.my_attr]

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr

class Cell:
    quantity1 = Discr()
    quantity2 = Discr()

    def __init__(self, quantity1, quantity2):
        self.quantity1 = quantity1
        self.quantity2 = quantity2

    def __add__(self, other):
        return other.quantity1 + other.quantity2

    def __sub__(self, other):
        if other.quantity1 - other.quantity2 > 0: return other.quantity1 - other.quantity2
        return 'Операция не выполняется'

    def __mul__(self, other):
        return other.quantity1 * other.quantity2

    def __truediv__(self, other):
        return other.quantity1 // other.quantity2

    def make_order(self, quantity, count):
        t = 0
        for i in range(quantity):
            print('*', end='')
            t+=1
            while t >= count:
                print('/n', end=' ')
                t = 0
        return ''

quantity = Cell(15, 5)
quantity.quantity1 = 15
quantity.quantity2 = 5
print(f'Складываем {(quantity.quantity1 + quantity.quantity2)}\n')
print(f'Вычитыаем \n{(quantity.quantity1 - quantity.quantity2)}\n')
print(f'Умножаем \n{(quantity.quantity1 * quantity.quantity2)}\n')
print(f'Делим \n{(quantity.quantity1 // quantity.quantity2)}\n')
print(quantity.make_order(22,5))