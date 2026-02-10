# def add(*args):
    # print(args) # Tuple
#     sum = 0
#     for n in args:
#         sum += n
#     print(sum)
#     # return print(sum(args))

# add(1,2,3,4,5,6,7,8,9)

def calculate(n, **kwargs):
    print(kwargs) # dictionary
    # for key, value in kwargs.items():
    #     print(key, value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colours = kw.get("colours")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan")
print(my_car.model)