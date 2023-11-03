# create the "Car" class
class Car:

    # define the __init__ method, passing year_model and make as arguments
    def __init__(self, year_model, make):
    
        # define data attributes, year_model, make, and speed
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0
        
    # define the accelerate method
    def accelerate(self):
        self.__speed += 5
    
    # define the brake method
    def brake(self):
        self.__speed -= 5
    
    # define the get_speed method
    def get_speed(self):
        return self.__speed
    
    # define a get_year_model method
    def get_year_model(self):
        return self.__year_model
    
    # define a get_make method
    def get_make(self):
        return self.__make