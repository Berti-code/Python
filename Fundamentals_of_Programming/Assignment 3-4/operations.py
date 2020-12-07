from entities import *
import copy

def print_list(list):
    for element in get_value(list):
            print(get_value(element))

def initialise(expenses_list):
    '''
    Initialises expenses_list with 10 initial values
    '''
    
    initial_values=[['add',100,'food'],['add',400,'taxes'],['add',50,'cleaning'],['add',50,'food'],['add',50,'books'],['add',20,'food'],['add',400,'internet'],['add',120,'shopping'],['add',250,'maintanace'],['add',5000,'repairs']]
    for i in range(len(initial_values)):
        add(expenses_list,initial_values[i])

def validate_command_arguments(expected_argumment_types,command_arguments):
    '''
    The function gets a list of expected_argumment_types and a list of command_arguments
    and changes each command argument into it's expected type
    '''
    if len(expected_argumment_types)!=len(command_arguments):
        return False
    for i in range(len(command_arguments)):
        try:
            type(expected_argumment_types[i](command_arguments[i]))
        except:
            return False
        else:
            return True

def list_with_comparison(expenses_list,given_command):
    '''
    The function shows the expenses that respect the comparison given in the command(<,=,>)
    '''
    for element in get_value(expenses_list):
        if given_command[2]=='<':
            if element['expense type']==given_command[1] and element['ammount of money'] < given_command[3]:
                print(get_value(element))
        if given_command[2]=='>':
            if element['expense type']==given_command[1] and element['ammount of money'] > given_command[3]:
                print(get_value(element))
        if given_command[2]=='=':
            if element['expense type']==given_command[1] and element['ammount of money'] == given_command[3]:
                print(get_value(element))

def list(expenses_list,given_command):
    '''
    The function shows all the expenses in the list
    '''
    if len(given_command)==1:
        print_list(expenses_list)
    elif len(given_command)==2:
        for element in get_value(expenses_list):
            if element['expense type']==given_command[1]:
                print(get_value(element))
    elif len(given_command)==4:
        if given_command[3].isdigit():
            given_command[3]=int(given_command[3])
            list_with_comparison(get_value(expenses_list),given_command)
        else:
            raise TypeError('Unexpected number of arguments!')  
    else:
        raise ValueError('Unexpected number of arguments!')

def get_curent_day():
    '''
    The function returns the curent day
    '''
    from datetime import date
    today=date.today()
    day=today.strftime("%d")
    return day

def add(expenses_list,given_command):
    '''
    The function adds a new expense to the list on the curent day
    '''
    keys=['day','ammount of money','expense type']
    expected_argument_types=[int,int,str]
    day=get_curent_day()
    given_command.insert(1,day)

    command_arguments=given_command[1:len(given_command)]
    for i in range(len(command_arguments)):
        command_arguments[i]=str(command_arguments[i])

    if validate_command_arguments(expected_argument_types,command_arguments)==True:
        set_expense(expenses_list,dict(zip(keys,command_arguments)))
        correct_type_of_values_in_dictionary(get_value(expenses_list)[len(get_value(expenses_list))-1],expected_argument_types,keys)
    else:
        raise TypeError('Unexpected type/number of arguments!')

def insert(expenses_list,given_command):
    '''
    The function adds a new expense to the list on a day given by the user
    '''
    keys=['day','ammount of money','expense type']
    expected_argument_types=[int,int,str]
    command_arguments=given_command[1:len(given_command)]
    
    for i in range(len(command_arguments)):
        command_arguments[i]=str(command_arguments[i])

    if validate_command_arguments(expected_argument_types,command_arguments)==True:
        if int(command_arguments[0])<=30 and int(command_arguments[0])>=1:
            set_expense(expenses_list,dict(zip(keys,command_arguments)))
            correct_type_of_values_in_dictionary(get_value(expenses_list)[len(get_value(expenses_list))-1],expected_argument_types,keys)
        else:
            raise ValueError('The given day is not between 1 and 30')
    else:
        raise TypeError('Unexpected type/number of arguments!')

def remove_to(expenses_list,given_command):
    '''
    The function removes all the expenses in the days between 2 days given in the command
    '''
    if given_command[2]=='to':
        try:
            if given_command[1].isdigit() and given_command[3].isdigit():
                    given_command[1]=int(given_command[1]) 
                    given_command[3]=int(given_command[3])
            if given_command[1]<0 and given_command[3]>30:
                raise ValueError('Invalid given days!')
        except:
            raise TypeError('Unexpected type of arguments!')
        else:
            for element in get_value(expenses_list)[:]:
                if given_command[1]<=element['day'] and given_command[3]>=element['day']:
                    get_value(expenses_list).remove(element)
    else:
        raise ValueError('Invalid command!')

def remove(expenses_list,full_given_command):
    '''
    The function removes all the expenses in the day or category given in the command
    '''
    if full_given_command[1].isdigit():
        field='day'
        full_given_command[1]=int(full_given_command[1])
    else:
        field='expense type'
    for element in get_value(expenses_list)[:]:
        if full_given_command[1] == element[field]:
            get_value(expenses_list).remove(element)

def remove_element(expenses_list,given_command):
    '''
    The function decides if a remove between 2 days operation has to be done or a remove
    by category/day
    '''
    if len(given_command)==2:
        remove(get_value(expenses_list),given_command)
        
    elif len(given_command)==4:
        remove_to(get_value(expenses_list),given_command)
    else:
        raise ValueError('Unexpected number of arguments!')

def sum(expenses_list,given_command):
    '''
    The function calculates the sum of all the expenses in a certain category
    '''
    sum=0
    if len(given_command)==2:
        for element in expenses_list:
            if element['expense type']==given_command[1]:
                sum+=element['ammount of money']
        print('Total expenses for given category=',sum)
    else:
        raise ValueError('Unexpected number of arguments!')

def validate_day(day):
    '''
    The function tests if int number is valid day
    '''
    if day>=0 and day<=30:
        return True
    else:
        return False

def max(expenses_list,given_command):
    '''
    The function calculates the maximum expense of the day
    '''
    maximum_expense_of_the_day=0
    if len(given_command)==2:
        if given_command[1].isdigit():
            day=int(given_command[1])
        else:
            raise TypeError('Unexpected command type!')
        if validate_day(day)==True:
            for element in expenses_list:
                if element['ammount of money']>maximum_expense_of_the_day:
                    maximum_expense_of_the_day=element['ammount of money']
                    dictionary_of_maximum_expense_of_the_day=element
            print('Maximum expense of the day:',dictionary_of_maximum_expense_of_the_day)
        else:
            raise TypeError('Invalid given day!')
    else:
        raise ValueError('Unexpected number of arguments!')

def sort(expenses_list,given_command):
    '''
    The function sorts the expenses for a category or day in ascending order by 
    amount of money 
    '''
    if len(given_command)==2:
        if given_command[1].isdigit():
            sort_by='day'
        else:
            sort_by='expense type'
        sorted_expenses_list=sorted(expenses_list[:],key=lambda i:i[sort_by])
        print_list(sorted_expenses_list)
    else:
        raise ValueError('Unexpected number of arguments!')

def filter_with_comparison(expenses_list,given_command):
    '''
    The function filters the expenses by category or filters the expenses by 
    category and by comparing the ammount of money with a sum given in the command
    '''
    result_of_filter=[]
    try:
        for element in expenses_list:
            if given_command[2]=='<':
                if element['expense type']==given_command[1] and element['ammount of money'] < given_command[3]:
                    result_of_filter.expenses_list(element)
            if given_command[2]=='>':
                if element['expense type']==given_command[1] and element['ammount of money'] > given_command[3]:
                    result_of_filter.expenses_list(element)
            if given_command[2]=='=':
                if element['expense type']==given_command[1] and element['ammount of money'] == given_command[3]:
                    result_of_filter.expenses_list(element)
        expenses_list[:]=result_of_filter

    except:
        raise ValueError('Incorect command!')

def filter_category(expenses_list,given_command):
    '''
    The function filters the expenses by a given category
    '''
    result_of_filter=[]
    for element in expenses_list:
        if element['expense type']==given_command[1]:
            result_of_filter.append(element)
    expenses_list[:]=result_of_filter

def filter(expenses_list,given_command):
    '''
    The function decides to either call filter by category or filter by 
    category and comparison unsing the number of given arguments
    '''
    if len(given_command)==2:
        filter_category(expenses_list,given_command)
    elif len(given_command)==4:
        print('!')
        if given_command[3].isdigit():
            given_command[3]=int(given_command[3])
            filter_with_comparison(expenses_list,given_command)
        else:
            raise TypeError('Unexpected type of arguments!')
    else:
        raise ValueError('Unexpected number of arguments!')

def add_curent_expenses_list_to_history(expenses_list,past_expenses):
    past_expenses.append(expenses_list[:])

def undo(expenses_list,past_expenses):
    '''
    The function undoes the last operation
    '''
    if len(past_expenses)>1:
        past_expenses.pop()
        expenses_list[:]=past_expenses[len(past_expenses)-1]
    else:
        raise ValueError('You have reached the initial values!')    