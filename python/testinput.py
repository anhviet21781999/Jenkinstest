class Car:
    """
    Car models a car w/ tires and an engine 
    """

    def __init__(self, engine, tires) :
   
        self.engine = engine
        self.tires = tires
# tao ra mot doi tuong car         
my_car = Car(engine="v6", tires=4)

print(my_car.engine)
print(my_car.tires)      
   