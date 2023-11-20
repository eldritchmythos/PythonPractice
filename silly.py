class Employee:
    
    def __init__(self, emp_name, emp_num):
        self.__emp_name = emp_name
        self.__emp_num = emp_num
        
    def set_emp_name(self, emp_name):
        self.__emp_name = emp_name
        
    def set_emp_num (self, emp_num):
        self.__emp_num = emp_num
    
    def get_emp_name(self):
        return self.__emp_name
    
    def get_emp_num(self):
        return self.__emp_num
    
# create the subclass, ProductionWorker
class ProductionWorker(Employee):
    
    #initialize data attributes for the productionworker subclass
    def __init__(self, emp_name, emp_num, shift, hourly_pay):
        #initialize the data attributes for the superclass
        Employee.__init__(self, emp_name, emp_num)
        
        #initialize subclasses data attributes
        
        self.__shift = shift
        self.__hourly_pay = hourly_pay
    
    #set mutator methods
    def set_shift(self, shift):
        self.__shift = shift
        
    def set_hourly_pay_rate(self, hourly_pay):
        self.__hourly_pay_rate = hourly_pay
    
    #set accessor methods   
    def get_shift(self):
        return self.__shift
    
    def get_hourly_pay(self):
        return self.__hourly_pay
