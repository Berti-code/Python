from operations import add,list,insert,remove_element,sum,max,sort,undo,filter
from operations import initialise,add_curent_expenses_list_to_history
from entities import get_value

def read_command():
    given_command=input('>>>')
    list_of_words=given_command.split()
    return list_of_words

def run_menu(expenses_list):
    past_expenses=[]
    initialise(expenses_list)
    add_curent_expenses_list_to_history(expenses_list,past_expenses)
    while True:
        command_options={'add':add,'list':list,'insert':insert,'remove':remove_element,'sum':sum,'max':max,'sort':sort,'filter':filter}
        given_command=read_command()

        try:
            if given_command[0]=='undo' and len(given_command)==1:
                undo(expenses_list,past_expenses)
            else:
                command_options[given_command[0]](get_value(expenses_list),given_command)
                if given_command[0] !='list':
                    add_curent_expenses_list_to_history(expenses_list,past_expenses)            
        except:
           raise ValueError("Not a valid command!")
        