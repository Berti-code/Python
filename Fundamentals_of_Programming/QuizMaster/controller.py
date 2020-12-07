class Controller:
    def __init__(self,repo):
        self.__repo=repo

    def validator_add(self,arguments_list):
        if len(arguments_list)!=7:
            raise ValueError('Incorrect number of arguments!')
        if arguments_list[6] not in ['easy','medium','hard']:
            raise ValueError('Incorrect dificulty!')
        if arguments_list[0].isdigit():
            arguments_list[0]=int(arguments_list[0])
        else:
            raise ValueError('Incorrect type of arguments!')

    def add_question(self,command):
        #add 1;text;choice_a;choiche_b;choice_c;correct_choice;easy
        arguments=command[1]
        arguments_list=arguments.split(sep=';')
        self.validator_add(arguments_list)
        self.__repo.append_master_question_list(arguments)
        print(arguments)

    def validator_create(self,arguments_list):
        #format incorrect or not enough easy questions => error, quiz not created
        if len(arguments_list)!=3:
            raise ValueError('Incorrect number of arguments!')
        if arguments_list[0] not in ['easy','medium','hard']:
            raise ValueError('Incorrect dificulty!')
        if arguments_list[1].isdigit():
            arguments_list[1]=int(arguments_list[1])
        #check number of questions
        question_list=self.__repo.get_master_question_list()
        number_of_questions_with_required_difficulty=0
        number_of_questions=len(question_list)
        if number_of_questions!=arguments_list[1]:
            raise ValueError('Invalid number of questions in command!')
        for question in question_list:
            question_fields=question.split(sep=';')
            if question_fields[6]==arguments_list[0]:
                number_of_questions_with_required_difficulty+=1
        if number_of_questions_with_required_difficulty<number_of_questions/2:
            raise ValueError('Not enough questions with required difficulty to create quiz!')


    def create_quiz(self,command):
        #create <difficulty> <number_of_questions> <file>
        print(command)
        lenght=len(command)
        arguments_list=command[1:lenght]
        print(arguments_list)
        self.validator_create(arguments_list)
        question_list=self.__repo.get_master_question_list()
        file_name=arguments_list[2]
        file=open(file_name,'a')
        for question in question_list:
            file.writelines(question+"\n")
        file.close()