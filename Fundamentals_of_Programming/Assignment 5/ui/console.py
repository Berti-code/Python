from services.ComplexNumber_service import Services
from domain.entities import ComplexNumber

class Console:
    def __init__(self,complex_number_service):
        self.__complex_number_service=complex_number_service
        self.__list_of_numbers=self.__complex_number_service.get_complex_numbers()
        self.__history_list=[]


    def add_number(self):
        real_part=int(input('real part='))
        imaginary_part=int(input('imaginary part='))
        self.__complex_number_service.add_complex_number(ComplexNumber(real_part,imaginary_part))

    def print_numbers(self):
        print('List of complex numbers:')
        i=0
        for number in self.__list_of_numbers:
            print('z[',i,']=',sep='',end='')
            print (number.real_part,end='')
            if number.imaginary_part>=0:
                print('+',end='')
            print (number.imaginary_part,'i',sep='')
            i+=1


    def filter(self):
        start_position=int(input('Starting position of the filter='))
        end_position=int(input('End position of the filter='))
        self.__list_of_numbers[:]=self.__list_of_numbers[start_position:end_position+1]

    def undo(self):
        if len(self.__history_list)>1:
            self.__history_list.pop()
            self.__list_of_numbers[:]=self.__history_list[-1]
        else:
            print('History list empty!')
            raise ValueError('Undo impossible to execute!')

    def add_to_history(self):
        self.__history_list.append(self.__list_of_numbers[:])

    def run_console(self):
        list_of_commands={1:self.add_number,2:self.print_numbers,3:self.filter,4:self.undo}
        self.add_to_history()
        while True:
            try:
                print(
                '''
                Program functionalities:
                1.Add a new complex number
                2.Show the list of numbers
                3.Filter list between given indeces
                4.Undo last operation
                ''')
                chosen_operation=input('Enter chosen operation:')
                chosen_operation=int(chosen_operation)
                list_of_commands[chosen_operation]()
                if chosen_operation == 1 or chosen_operation == 3:
                    self.add_to_history()
                
            except:
                print('Operation failed!')