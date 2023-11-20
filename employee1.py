# Create a class
class Employee:
    
    # initialize the data attributes for the employee class
    def __init__(self, emp_name, emp_num):
        self.__emp_name = emp_name
        self.__emp_num = emp_num
        
    # define mutator methods for emp_name data attribute
    def set_emp_name(self, emp_name):
        self.__emp_name = emp_name
    
    # define mutator methods for emp_num data attribute
    def set_emp_num(self, emp_num):
        self.__emp_num = emp_num
    
    # define accessor methods for emp_name attribute
    def get_emp_name(self):
        return self.__emp_name
    
    # define accessor methods for emp_num attribute
    def get_emp_num(self):
        return self.__emp_num
    

# Create the ShiftSupervisor subclass
class ShiftSupervisor(Employee):

    # Initialize inherited and new data attributes for the new subclass
    def __init__(self, emp_name, emp_num, annual_salary, annual_production_bonus):
        
        # Initialize the data attributes for the superclass
        super().__init__(emp_name, emp_num)
        
        # Initialize the new data attributes
        self.__annual_salary = annual_salary
        self.__annual_production_bonus = annual_production_bonus
    
    # define mutator methods for data attributes
    def set_annual_salary(self, annual_salary):
        self.__annual_salary = annual_salary
        

    def set_annual_production_bonus(self, annual_production_bonus):
        self.__annual_production_bonus = annual_production_bonus
        
    
    # define the accessor methods
    def get_annual_salary(self):
        return self.__annual_salary
    
    
    def get_annual_production_bonus(self):
        return self.__annual_production_bonus
    