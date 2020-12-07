from domain.entities import ComplexNumber

class Services:
    
    def __init__(self):
        #creates a list of complex numbers and it initialises it with 10 values
        self.__complex_numbers=[]
        for number in range(10):
            self.__complex_numbers.append(ComplexNumber(number,number+2))

    def add_complex_number(self,complex_number):
        #adds a new complex number to the list
        #complex_number - (type ComplexNumber) the complex number to be added
        self.__complex_numbers.append(complex_number)

    def get_complex_numbers(self):
        #returns the list of complex numbers
        return self.__complex_numbers