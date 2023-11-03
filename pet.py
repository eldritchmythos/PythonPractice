# create a class called "Pet"
class Pet:
    
    # define the init method
    def __init__(self, name, animal_type, age): 
        
        #create data attributes "name", "animal_type", and "age"
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age
        
    # define the mutator methods where we will store values in the data attributes
    
    # define the set_name method, this assigns a value to the __name field
    #This seems redundant to me, but the question required it
    def set_name(self,name):
        self.__name = name
    
    
    # define the set_animal_type method, this assigns a value to the __animal_type field
    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type
    
    
    # define the set_age method, this assigns a value to the __age field
    def set_age (self, age):
        self.__age = age
    
    
    # define the accessor methods where we will return the values from the data attributes
    
    # define the get_name method, this returns the value of the __name field
    def get_name(self):
        return self.__name
    
    
    # define the get_animal_type method, this returns the value of the __animal_type field
    def get_animal_type(self):
        return self.__animal_type
    
    
    # define the get_age method
    def get_age(self):
        return self.__age
    