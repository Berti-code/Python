from entities import correct_type_of_values_in_dictionary,set_expense
from operations import remove,remove_to


def call_tests():
    #function calls test functions
    set_expense__dictionary__true()
    remove_by_day__int__true()
    remove_between_days__2dictionaries__true()
    test_remove_by_category_true()

def set_expense__dictionary__true():
    #function that testes the set_expense function
    expense={}
    set_expense(expense,{'expense type': 'food', 'ammount of money': 200, 'day': 21})
    assert int(expense["day"])==21
    assert int(expense["amount"])==200
    assert int(expense["expense_type"])=="food"

def remove_by_day__int__true():
    #function that testes the remove function when called with an int
    expense=[]
    set_expense(expense,{'expense type': 'internet', 'ammount of money': 200, 'day': 12})
    test_list=[]
    test_list.append(expense)
    remove(test_list, 12)
    assert expense not in test_list

def remove_between_days__2dictionaries__true():
    #function that tastes remove_to function
    test_list=[]
    expense1=[]
    expense2=[]
    set_expense(expense1,{'expense type': 'internet', 'ammount of money': 200, 'day': 25})
    test_list.append(expense1)
    set_expense(expense2,{'expense type': 'internet', 'ammount of money': 200, 'day': 8})
    test_list.append(expense2)
    remove_to(test_list, 'remove 19 to 29')
    assert expense1 not in test_list
    assert expense2 in test_list

def test_remove_by_category_true():
    #function that testes the remove function when called with a str
    test_list=[]
    expense1=[]
    expense2=[]
    set_expense(expense1,{'expense type': 'internet', 'ammount of money': 200, 'day': 12})
    set_expense(expense2,{'expense type': 'internet', 'ammount of money': 200, 'day': 16})
    test_list.append(expense1)
    test_list.append(expense2)
    remove(test_list, "internet")
    assert expense1 not in test_list
    assert expense2 in test_list
    