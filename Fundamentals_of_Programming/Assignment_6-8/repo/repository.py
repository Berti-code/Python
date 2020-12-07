from domain.domain import Movie,Client,Rental
from exceptions.exceptions import NotFound
from datetime import date
import datetime


class MovieRepo:
    def __init__(self):
        self.__movie_list=[]
        self.initialise_list()

    def initialise_list(self):
        initial_movies=[
            ['The Shawshank Redemption','Two imprisoned men bond over a number of years.','Drama'],
            ['The Godfather','The aging mob boss transfers control to his reluctant son.','Crime'],
            ['The Lord of the Rings: The Return of the King','The former Fellowship members prepare for the final battle.','Adventure'],
            ['Pulp Fiction','The lives of the characters intertwine in four tales of violence and redemption.','Crime'],
            ['Schindler\'s List','Oskar Schindler gradually becomes concerned for his Jewish workforce','Biography'],
            ['Fight club','The characters form an underground fight club that evolves into something much, much more.','Drama'],
            ['Forrest Gump','History unfolds through the perspective of an Alabama man with an IQ of 75.','Drama'],
            ['Goodfellas','The story of an Italian-American crime syndicate.','Crime'],
            ['American History X','A former neo-nazi skinhead tries to save his younger brother.','Drama'],
            ['Synecdoche, New York','A theatre director struggles with his work, and the women in his life, as he creates a life-size replica of New York City inside a warehouse as part of his new play.','Drama']
        ]
        id=1000
        for movie in initial_movies:
            self.__movie_list.append(Movie(id,movie[0],movie[1],movie[2]))
            id+=1

    def get_movie_list(self):
        return self.__movie_list

    def find_movie(self,movieId):
        for i in range(len(self.__movie_list)):
            if self.__movie_list[i]._id == movieId:
                return i
        raise NotFound('Movie not found!')

    def add(self,movie):
        self.__movie_list.append(movie)

    def delete_movie(self,delete_id):
        self.__movie_list.pop(self.find_movie(delete_id))

    def update_movie(self,movie_id,new_title,new_description,new_genre):
        index=self.find_movie(movie_id)
        self.__movie_list[index].set_title(new_title)
        self.__movie_list[index].set_description(new_description)
        self.__movie_list[index].set_genre(new_genre)


class ClientRepo:
    def __init__(self):
        self.__client_list=[]
        self.initialise_list()

    def initialise_list(self):
        initial_clients_first_name=['Oliver','Jack','Harry','Jacob','Charlie','Amelia','Olivia','Emily','Isabella','Jessica']
        initial_clients_last_name=['Smith','Murphy','Jones','O\'Kelly','Johnson','Williams','O\'Sullivan','Roberts','Morton','Wilson']
        id=1000
        for index in range(len(initial_clients_first_name)):
            self.__client_list.append(Client(id,initial_clients_first_name[index] + ' ' + initial_clients_last_name[index]))
            id+=1

    def get_client_list(self):
        return self.__client_list

    def find_client(self,clientId):
        for i in range(len(self.__client_list)):
            if self.__client_list[i]._id == clientId:
                return i
        raise NotFound('Client not found!')

    def add(self,client):
        self.__client_list.append(client)

    def delete_client(self,delete_id):
        self.__client_list.pop(self.find_client(delete_id))

    def update_client(self,client_id,new_name):
        index=self.find_client(client_id)
        self.__client_list[index].set_name(new_name)


class RentalRepo:
    def __init__(self):
        self.__rental_list=[]
        self.initialise_list()

    def initialise_list(self):
        initial_rentals=[
            [1000,1005,'2019-10-26','2019-12-02'],
            [1001,1006,'2019-11-09','2019-12-28'],
            [1002,1008,'2019-11-21','2020-12-21'],
            [1003,1004,'2019-11-25','2020-02-25'],
            [1004,1003,'2019-02-11','2020-02-11'],
            [1005,1000,'2019-09-26','2020-02-13'],
            [1006,1001,'2019-11-15','2019-12-02'],
            [1007,1009,'2019-11-29','2020-02-19'],
            [1008,1002,'2019-02-18','2020-01-10'],
            #[1009,1007,'2019-12-02','2019-12-31'],
        ]
        id=1000
        for rental in initial_rentals:
            due_date=datetime.datetime.strptime(rental[2], '%Y-%m-%d').date()
            rented_date=datetime.datetime.strptime(rental[3], '%Y-%m-%d').date()
            self.__rental_list.append(Rental(id,rental[0],rental[1],due_date,rented_date))
            id+=1

    def get_rental_list(self):
       return self.__rental_list

    def add_rental(self,rental):
        self.__rental_list.append(rental)

    def find_rental(self,rentalId):
        for i in range(len(self.__rental_list)):
            if self.__rental_list[i].get_rentalId()  == rentalId:
                return self.__rental_list[i]

    def find_rental_index(self,movieId):
        for i in range(len(self.__rental_list)):
            if self.__rental_list[i].get_movieId() == movieId:
                if self.__rental_list[i].get_returned_date() == None:
                    return i
        raise NotFound('Rental not found!')

    def return_movie(self,movieId):
        index=self.find_rental_index(movieId)
        self.__rental_list[index].set_returned_date(date.today())