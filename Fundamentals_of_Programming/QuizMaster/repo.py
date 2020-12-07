class Repo:
    def __init__(self):
        self.__master_question_list=[]

    def get_master_question_list(self):
        return self.__master_question_list

    def append_master_question_list(self,question):
        self.__master_question_list.append(question)