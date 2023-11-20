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
    
# create a subclass called ProductionWorker
class ProductionWorker(Employee):
    
    # initialize data attributes for the subclass
    def __init__(self, emp_name, emp_num, shift, hourly_pay):
        
        # initialize the data attributes for superclass
        Employee.__init__(self,emp_name, emp_num)
        
        # initialize data attributes for subclass
        self.__shift = shift
        self.__hourly_pay = hourly_pay
        
    # define mutator methods for shift data attribute
    def set_shift(self, shift):
        self.__shift = shift
    
    # define mutator methods for hourly_pay data attribute   
    def set_hourly_pay(self, hourly_pay):
        self.__hourly_pay = hourly_pay
        
    # define accessor methods for the shift and hourly_pay attributes
    def get_shift(self):
        return self.__shift
    
    def get_hourly_pay(self):
        return self.__hourly_pay
    