from service.service import Service
import os


class Console:
    def __init__(self,service):
        self.__service=service

    #movie UI methods:
    def add_movie_console(self):
        #adds movie to list
        movieId=int(input('MovieID:'))
        title=input('Title:')
        description=input('Description:')
        genre=input('Genre:')
        self.__service.add_movie(movieId,title,description,genre)

    def remove_movie_console(self):
        #removes a movie from the list
        remove_movieId=int(input('Remove movie with movieID:'))
        self.__service.remove_movie(remove_movieId)

    def update_movie_console(self):
        #updates movie information
        update_movieId=int(input('Update movie with movieID:'))
        new_title=input('Title:')
        new_description=input('Description:')
        new_genre=input('Genre:')
        self.__service.update_movie(update_movieId,new_title,new_description,new_genre)

    def list_movie_console(self):
        #prints movies
        movie_list=self.__service.get_movies_list()
        for movie in movie_list:
            print('ID:',movie.get_id())
            print('Title:',movie.get_title())
            print('Description:',movie.get_description())
            print('Genre:',movie.get_genre())
            print()


    def most_rented_movies(self):
        #sorts list and then prints the movies in the required order
        sorted_movie_list,movieId_list=self.__service.most_rented_movies()
        i=0
        for movie in sorted_movie_list:
            print('ID:',movie.get_id())
            print('Title:',movie.get_title())
            print('Description:',movie.get_description())
            print('Genre:',movie.get_genre())
            print('Number of days rented:',movieId_list[i][1])
            print()
            i+=1

    #client UI methods:
    def add_client_console(self):
        #adds client to list
        clientId=int(input('ClientID:'))
        name=input('Name:')
        self.__service.add_client(clientId,name)

    def remove_client_console(self):
        #removes client from list
        remove_clientId=int(input('Remove client with clientID:'))
        self.__service.remove_client(remove_clientId)

    def update_client_console(self):
        #updates client information
        update_clientId=int(input('Update client with clientID:'))
        new_name=input('Name:')
        self.__service.update_client(update_clientId,new_name)

    def list_client_console(self):
        #prints clients
        client_list=self.__service.get_clients_list()
        for client in client_list:
            print()
            print('ID:',client.get_id())
            print('Name:',client.get_name())

    def most_active_clients(self):
        #sorts list and then prints the movies in the required order
        sorted_client_list,clientId_list=self.__service.most_active_clients()
        i=0
        for client in sorted_client_list:
            print('ID:',client.get_id())
            print('Name:',client.get_name())
            print('Number of days rented:',clientId_list[i][1])
            print()
            i+=1

    def search_client(self):
        search_string=input('Search for:')
        search_result=self.__service.search_client(search_string)
        for client in search_result:
            print('ID:',client.get_id())
            print('Name:',client.get_name())
            print()

    #rental UI methods:
    def add_rental_console(self):
        clientId=int(input('ClientID:'))
        movieId=int(input('Rent movie with movieID:'))
        due_date=input('Due date as \'YYYY-MM-DD\':')
        self.__service.add_rental(clientId,movieId,due_date)

    def return_movie_rental_console(self):
        movieId=int(input('MovieID of movie to return:'))
        self.__service.return_movie_rental(movieId)

    def list_rentals(self):
        rental_list=self.__service.get_rentals_list()
        for rental in rental_list:
            print('RentalID:',rental.get_rentalId())
            print('MovieID:',rental.get_movieId())
            print('ClientID:',rental.get_clientId())
            print('Date of rental:',rental.get_rented_date())
            print('Due date:',rental.get_due_date())
            print('Returned date:',rental.get_returned_date())
            print()
    
    def list_late_rentals(self):
        sorted_late_rentals,rentalId_list=self.__service.late_rentals()
        i=0
        for rental in sorted_late_rentals:
            print('RentalID:',rental.get_rentalId())
            print('MovieID:',rental.get_movieId())
            print('ClientID:',rental.get_clientId())
            print('Date of rental:',rental.get_rented_date())
            print('Due date:',rental.get_due_date())
            print('Returned date:',rental.get_returned_date())
            print('Delay in number of days:',rentalId_list[i][1])
            print()
            i+=1
        
    #UI messages:

    def main_menu_message(self):
        print('''\nProgram functionalities:
        1 - add movie/client
        2 - remove movie/client
        3 - update movie/client
        4 - list movie/client
        5 - rent
        6 - return movie
        7 - list rentals
        8 - most rented movies
        9 - most active clients
        10 - late rentals
        11 - search movie/client
        ''')

    def client_or_movie_message(self):
        print('''
        1 - movie
        2 - client''')


    def run_menu(self):
        movie_operations={1:self.add_movie_console,2:self.remove_movie_console,3:self.update_movie_console,4:self.list_movie_console}
        client_operations={1:self.add_client_console,2:self.remove_client_console,3:self.update_client_console,4:self.list_client_console,11:self.search_client}
        other_operations={5:self.add_rental_console,6:self.return_movie_rental_console,7:self.list_rentals,8:self.most_rented_movies,
        9:self.most_active_clients,10:self.list_late_rentals}
        while True:
            #try:
            self.main_menu_message()
            chosen_operation=input('>>>')
            chosen_operation=int(chosen_operation)
            os.system('clear')
            self.main_menu_message()
            #print('>>>',chosen_operation)
            if (chosen_operation >= 1 and chosen_operation <= 4) or chosen_operation==11:
                self.client_or_movie_message()
                client_or_movie_choise=int(input('>>>'))
                if client_or_movie_choise == 1:
                    movie_operations[chosen_operation]()
                elif client_or_movie_choise == 2:
                    client_operations[chosen_operation]()
                else:
                    raise Exception('Invalid option!')
            else:
                    other_operations[chosen_operation]()
            #except Exception as e:
             #   print(e)