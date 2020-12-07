#getters/setters
def get_value(variable):
    return variable

def set_expense(expenses_list,values):
    expenses_list.append(values)

def correct_type_of_values_in_dictionary(dictionary,expected_argument_types,keys):
    for i in range(len(keys)):
        dictionary[keys[i]]=expected_argument_types[i](dictionary[keys[i]])        