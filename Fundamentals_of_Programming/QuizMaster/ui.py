class Ui:
    def __init__(self,controller):
        self.__controller=controller
    
    def add_question(self,command):
        self.__controller.add_question(command)
        print('Question added!')

    def create_quiz(self,command):
        self.__controller.create_quiz(command)
        print('Quiz file created!')

    def run_app(self):
        #try except
        functionalities={'add':self.add_question,'create':self.create_quiz}
        while True:
            print('''
            Commands:
            add <id>;<text>;<choice_a>;<choiche_b>;<choice_c>;<correct_choice>;<difficulty>
            create <difficulty> <number_of_questions> <file>
                --difficulty=['easy','medium','hard']
            ''')
            string=input('>>>')
            command=string.split()
            option=command[0]
            functionalities[option](command)