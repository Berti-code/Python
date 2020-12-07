class Movie:
    def __init__(self,movieId,title,description,genre):
        self._id=movieId
        self._title=title
        self._description=description
        self._genre=genre

    def get_id(self):
        return self._id
    
    def get_title(self):
        return self._title

    def get_description(self):
        return self._description

    def get_genre(self):
        return self._genre

    def set_id(self,id):
        self._id=id
    
    def set_title(self,title):
        self._title=title

    def set_description(self,description):
        self._description=description

    def set_genre(self,genre):
        self._genre=genre


class Client:
    def __init__(self,clientId,name):
        self._id=clientId
        self._name=name

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def set_id(self,id):
        self._id=id

    def set_name(self,name):
        self._name=name

class Rental:
    def __init__(self,rentalId,movieId,clientId,rented_date,due_date):
        self._rental_id=rentalId
        self._movie_id=movieId
        self._client_id=clientId
        self._rented_date=rented_date
        self._due_date=due_date
        self._returned_date=None

    def get_rentalId(self):
        return self._rental_id

    def get_movieId(self):
        return self._movie_id

    def get_clientId(self):
        return self._client_id

    def get_rented_date(self):
        return self._rented_date

    def get_due_date(self):
        return self._due_date

    def get_returned_date(self):
        return self._returned_date

    def set_returned_date(self,value):
        self._returned_date=value
