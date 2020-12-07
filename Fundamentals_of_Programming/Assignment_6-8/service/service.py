from domain.domain import Movie,Client,Rental
from datetime import date
from exceptions.exceptions import BadOperation,BadInput,NotFound
import datetime


class Service:
    def __init__(self,movie_repo,client_repo,rental_repo):
        self.__movies_repo=movie_repo
        self.__clients_repo=client_repo
        self.__rentals_repo=rental_repo

    def get_movies(self):
        return self.__movies_repo

    def get_clients(self):
        return self.__clients_repo

    def get_rentals(self):
        return self.__rentals_repo

    #get lists
    def get_movies_list(self):
        return self.get_movies().get_movie_list()

    def get_clients_list(self):
        return self.get_clients().get_client_list()

    def get_rentals_list(self):
        return self.get_rentals().get_rental_list()

    #methods for Movie:

    def add_movie(self,movieId,title,description,genre):
        movie=Movie(movieId,title,description,genre)
        self.__movies_repo.add(movie)

    def remove_movie(self,remove_movieId):
        self.__movies_repo.delete_movie(remove_movieId)

    def update_movie(self,clientId,new_title,new_description,new_genre):
        self.__movies_repo.update_movie(clientId,new_title,new_description,new_genre)

    def create_list_of_movieId(self):
        #creates a list of the movieId of each rental
        movieId_list=[]
        for rental in self.get_rentals_list():
            if rental._movie_id  not in movieId_list:
                movieId_list.append(rental._movie_id)
        return movieId_list

    def create_ordered_list_of_movies(self,movieId_list):
        #create a new list of movies using the order of the sorted list
        ordered_movie_list=[]
        for element in movieId_list:
            index=self.__movies_repo.find_movie(element[0])
            ordered_movie_list.append(self.get_movies_list()[index])
        return ordered_movie_list

    def most_rented_movies(self):
        #sorted  in  descending  order  of the number of days they were rented
        movieId_list=self.create_list_of_movieId()

        #appends to each id the number of days that movie was rented
        for i in range(len(movieId_list)):
            for rental in self.get_rentals_list():
                number_of_days_rented=0
                if rental.get_movieId() == movieId_list[i]:
                    if rental.get_returned_date() == None:
                        days_delta=date.today()-rental.get_rented_date()
                        number_of_days_rented+=days_delta.days
                    else:
                        days_delta=rental.get_returned_date()-rental.get_rented_date()
                        number_of_days_rented+=days_delta.days
                    movieId_list[i]=[movieId_list[i] , number_of_days_rented]
        #sort the list in descending order by number of days a movie was rented
        movieId_list.sort(key=lambda x: x[1],reverse=1)

        ordered_movie_list=self.create_ordered_list_of_movies(movieId_list)
        
        return ordered_movie_list,movieId_list


    #methods for Client:

    def add_client(self,clientId,name):
        client=Client(clientId,name)
        self.__clients_repo.add(client)

    def remove_client(self,remove_clientId):
        self.__clients_repo.delete_client(remove_clientId)

    def update_client(self,clientId,new_name):
        self.__clients_repo.update_client(clientId,new_name)

    def create_list_of_clientId(self):
        #creates a list of the clientId of each rental
        clientId_list=[]
        for rental in self.get_rentals_list():
            if rental._client_id  not in clientId_list:
                clientId_list.append(rental._client_id)
        return clientId_list

    def create_ordered_list_of_clients(self,clientId_list):
        #create a new list of movies using the order of the sorted list
        ordered_client_list=[]
        for element in clientId_list:
            index=self.__clients_repo.find_client(element[0])
            ordered_client_list.append(self.get_clients_list()[index])
        return ordered_client_list

    def most_active_clients(self):
        #list of clients, sorted in descending order of the number of movie rental days 
        # they have ;having 2 rented movies for 3 days eachcounts as 2 x 3 = 6

        clientId_list=self.create_list_of_clientId()

        #appends to each id the number of days that movie was rented
        for i in range(len(clientId_list)):
            for rental in self.get_rentals_list():
                number_of_days_rented=0
                if rental.get_clientId() == clientId_list[i]:
                    if rental.get_returned_date() == None:
                        days_delta=date.today()-rental.get_rented_date()
                        number_of_days_rented+=days_delta.days
                    else:
                        days_delta=rental.get_returned_date()-rental.get_rented_date()
                        number_of_days_rented+=days_delta.days
                    clientId_list[i]=[clientId_list[i] , number_of_days_rented]
        #sort the list in descending order by number of days a movie was rented
        clientId_list.sort(key=lambda x: x[1],reverse=1)

        ordered_client_list=self.create_ordered_list_of_clients(clientId_list)
        
        return ordered_client_list,clientId_list

    def search_client(self,search_string):
        search_result_list=[]
        clients=self.get_clients_list()
        for client in clients:
            name=client.get_name().split()
            first_name=name[0]
            family_name=name[1]
            client_id=client._id
            client_id=str(client_id)
            if client_id.find(search_string) != -1:     
                search_result_list.append(client)   
            elif  family_name.lower().find(search_string.lower()) != -1 or  first_name.lower().find(search_string.lower()) != -1:
                search_result_list.append(client)
        return search_result_list


    #methods for Rental:

    def convert_to_datetime(self,date_str):
        #'2019-11-29' -> '%Y-%m-%d'
        try:
            date_time_due_date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
        except:
            raise BadInput('Given datetime doesn\'t respect format!')
        return date_time_due_date

    def check_client_rentals(self,clientId):
        for rental in self.get_rentals_list():
            if int(rental.get_clientId()) == clientId:
                due_date_datetime=rental.get_due_date()
                current_date=date.today()
                if due_date_datetime < current_date:
                    raise BadOperation('Client has unreturned movies past due date!')

    def check_movie_availability(self,movieId):
        for rental in self.get_rentals_list():
            if int(rental.get_movieId()) == movieId:
                if rental.get_returned_date() == None:
                    raise BadOperation('Movie unavailable!')
    

    def add_rental(self,clientId,movieId,due_date_string):
        due_date=self.convert_to_datetime(due_date_string)
        #assign value to rentalId
        if len(self.get_rentals_list())==0:
            rentalId=1000
        else:
            rentalId=self.get_rentals_list()[-1]._rental_id + 1

        self.check_movie_availability(movieId)
        self.check_client_rentals(clientId)

        rental=Rental(rentalId,movieId,clientId,date.today(),due_date)  
        self.__rentals_repo.add_rental(rental)

    def return_movie_rental(self,movieId):
        self.__rentals_repo.return_movie(movieId)

    def create_list_of_rentalId(self):
        rentalId_list=[]
        for rental in self.get_rentals_list():
            if rental.get_due_date() < date.today():
                rentalId_list.append(rental.get_rentalId())
        return rentalId_list

    def create_ordered_list_of_rentals(self,rentalId_list):
        #create a new list of rentals using the order of the sorted list
        ordered_rental_list=[]
        for element in rentalId_list:
            rental=self.__rentals_repo.find_rental(element[0])
            ordered_rental_list.append(rental)
        return ordered_rental_list

    def late_rentals(self):
        #print the rentals for wich the due date has passed
        #sorted in decreasing order of the number of days of delay
        
        rentalId_list=self.create_list_of_rentalId()

        #appends to each id the delay in number of days
        for i in range(len(rentalId_list)):
            delay=0
            rental=self.__rentals_repo.find_rental(rentalId_list[i])
            if rental.get_rentalId() == rentalId_list[i]:
                if rental.get_returned_date() == None:
                    days_delta=date.today()-rental.get_due_date()
                    delay+=days_delta.days
                rentalId_list[i]=[rentalId_list[i] , delay]
        #sort the list in descending order by number of days a movie was rented
        rentalId_list.sort(key=lambda x: x[1],reverse=1)

        ordered_rental_list=self.create_ordered_list_of_rentals(rentalId_list)
        
        return ordered_rental_list,rentalId_list
