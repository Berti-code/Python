import math
def get_value(value):
    return value 

def get_real_part(list,index):
    return int(list[index][0])

def get_imaginary_part(list,index):
    return int(list[index][1])

def initial_values(list):
    values=[[8,8],[18,17],[1,1],[3,4],[3,-4],[-2,-6],[15,5],[8,8],[18,17],[8,8],[18,17]]
    for i in range(len(values)):
        add_number_to_list(list,create_complex_number(values[i][0],values[i][1]))

def create_complex_number(real_part,imaginary_part):
    return [real_part,imaginary_part]

def add_number_to_list(list,complex_number):
    list.append(complex_number)

def read_list(list):
    lenght_of_list=int(input("Number of complex numbers="))
    for i in range(lenght_of_list):
        print('z[',i,']:',sep='')
        real_part=int(input("Real part="))
        imaginary_part=int(input("Imaginary part="))
        add_number_to_list(list,create_complex_number(real_part,imaginary_part))
    
def print_list(list):
    print('List of complex numbers:')
    for i in range(len(list)):
        print('z[',i,']=',sep='',end='')
        print (get_real_part(list,i),end='')
        if get_imaginary_part(list,i)>=0:
            print('+',end='')
        print (get_imaginary_part(list,i),'i',sep='')

    
def return_positions_of_longest_sequence_of_ones_in_boolean_list(list):
    #this method gets a boolean list as a parameter and it returns the last position
    #and the lenght of the longest sequence of ones
    curent_sequence_lenght=0
    maximum_sequence_lenght=0
    last_position_of_maximum_sequence=0
    for i in range(len(list)):
        if get_value(list[i])==1:
            curent_sequence_lenght+=1
        if (get_value(list[i])==0 and get_value(list[i-1])==1) or i==len(list)-1:
            if curent_sequence_lenght>maximum_sequence_lenght:
                maximum_sequence_lenght=curent_sequence_lenght
                if i==len(list)-1:
                    last_position_of_maximum_sequence=i
                else:
                    last_position_of_maximum_sequence=i-1
            curent_sequence_lenght=0
            
    return last_position_of_maximum_sequence,maximum_sequence_lenght

def create_boolean_list_of_elements_with_modulus_between_0and10(list):
    #creates a boolean list, checking the element's with modulus in the [0, 10] range
    boolean_list=[]
    for i in range(len(list)):
        modulus_of_element=math.sqrt(get_real_part(list,i)**2+get_imaginary_part(list,i)**2)
        if modulus_of_element>=0 and modulus_of_element<=10:
            boolean_list.append(1)
        else:
            boolean_list.append(0)
    return boolean_list

def compose_result_sequence_of_elements_with_modulus_between_0and10(list):
    #this method gets the list as a parameter and composes a list using the last position
    #and the lenght of the longest sequence
    result_sequence=[]
    last_position_of_largest_sequence,maximum_sequence_lenght=return_positions_of_longest_sequence_of_ones_in_boolean_list(create_boolean_list_of_elements_with_modulus_between_0and10(list))
    first_position_of_largest_sequence=last_position_of_largest_sequence-maximum_sequence_lenght+1
    for i in range(first_position_of_largest_sequence,last_position_of_largest_sequence+1):
        result_sequence.append(get_value(list[i]))
    return result_sequence

def print_sequence(sequence):
    for i in range(len(sequence)):
            print (get_real_part(sequence,i),end='')
            if get_imaginary_part(sequence,i)>=0:
                print('+',end='')
            print (get_imaginary_part(sequence,i),'i',sep='',end='  ')

def sequence_with__modulus_between_0and10(list):
    #The modulus of all elements is in the [0, 10] range
    result_sequence=[]
    result_sequence=compose_result_sequence_of_elements_with_modulus_between_0and10(list)
    print('Longest sequence with the modulus of all elements in the [0, 10] range:')
    print_sequence(result_sequence)
        

def sum(first_complex_number,second_complex_number):
    result=[]
    result.append(first_complex_number[0]+second_complex_number[0])
    result.append(first_complex_number[1]+second_complex_number[1])
    return result

def create_boolean_list_with_equal_sum_of_consecutive_number_pairs(list,start_position):
    #creates a boolean list, checking the element's that are part of consecutive
    #number pairs that have equal sum
    boolean_list=[0]
    if start_position==4:
        boolean_list.append(0)
    for i in range (start_position,len(list),2):
        
        if sum(list[i],list[i-1])==sum(list[i-2],list[i-3]):
            boolean_list.append(1)
            boolean_list.append(1)
        else:
            boolean_list.append(0)
            boolean_list.append(0)
    boolean_list.append(0)
    print(boolean_list)
    return boolean_list

def sequence_with_equal_sum_of_consecutive_number_pairs(list):
    #Consecutive number pairs have equal sum.
    result_sequence=[]
    result_sequence=compose_result_sequence_with_equal_sum_of_consecutive_pairs(list)
    print('Longest sequence of consecutive number pairs that have equal sum:')
    print_sequence(result_sequence)
    

def compose_result_sequence_with_equal_sum_of_consecutive_pairs(list):
    #this method gets the list as a parameter and composes a sequence using the last 
    #position and the lenght of the longest sequence, taking into account the possible
    #pairs that can either start on even or uneven indexes
    result_sequence=[]
    last_position_of_largest_sequence_on_uneven_indexes,largest_sequence_lenght_on_uneven_indexes=return_positions_of_longest_sequence_of_ones_in_boolean_list(create_boolean_list_with_equal_sum_of_consecutive_number_pairs(list,3))
    last_position_of_largest_sequence_on_even_indexes,largest_sequence_lenght_on_even_indexes=return_positions_of_longest_sequence_of_ones_in_boolean_list(create_boolean_list_with_equal_sum_of_consecutive_number_pairs(list,4))
    print(largest_sequence_lenght_on_even_indexes,largest_sequence_lenght_on_uneven_indexes)
    
    if largest_sequence_lenght_on_even_indexes>largest_sequence_lenght_on_uneven_indexes:
        last_position_of_largest_sequence=last_position_of_largest_sequence_on_even_indexes
        largest_sequence_lenght=largest_sequence_lenght_on_even_indexes
    else:
        last_position_of_largest_sequence=last_position_of_largest_sequence_on_uneven_indexes
        largest_sequence_lenght=largest_sequence_lenght_on_uneven_indexes

    if largest_sequence_lenght>0:
        for i in range(last_position_of_largest_sequence-largest_sequence_lenght-1,last_position_of_largest_sequence+1):
            result_sequence.append(list[i])
        return result_sequence 


def run_menu(list):
    
    options={1:read_list,2:print_list,3:sequence_with__modulus_between_0and10,4:sequence_with_equal_sum_of_consecutive_number_pairs}
    option=0
    while True:
        print()
        print("""\nMenu options:
        Select 1 for reading a list of complex numbers.
        Select 2 for displaying the entire list of numbers on the console.
        Select 3 for displaying  on  the console  the  longest  sequence  in wich 
                 the modulus of all elements is in the [0, 10] range.
        Select 4 for displaying  on  the console  the  longest  sequence of elements
                 with equal sum of consecutive pairs.
        Select 5 for exiting the program.
        """)
        option=int(input('Select option:'))
        if option==5:
            return
        else:
            print('\nOperation results:')
            options[option](list)
        
if __name__=='__main__':
    list=[]
    initial_values(list)
    run_menu(list)