from repo.repository import MovieRepo,ClientRepo,RentalRepo
from domain.domain import Movie,Client,Rental
from service.service import Service
from ui.console import Console

test_movie_repository=MovieRepo()
test_client_repository=ClientRepo()
test_rental_repository=RentalRepo()

test_service=Service(test_movie_repository,test_client_repository,test_rental_repository)

def run_tests():
    test_add_movie_ValidInput_MovieAdded()
    test_update_movie_ValidInput_MovieUpdated()
    test_remove_movie_ValidInput_MovieRemoved()
    test_add_client_ValidInput_ClientAdded()
    test_update_client_ValidInput_ClientUpdated()
    test_remove_client_ValidInput_ClientRemoved()
    test_add_movie_InvalidInput_Error()
    test_add_client_InvalidInput_Error()
    test_update_movie_InvalidInput_Error()
    test_update_client_InvalidInput_Error()
    test_remove_movie_InvalidInput_Error()
    test_remove_client_InvalidInput_Error()

#Movie_Tests:
def test_add_movie_ValidInput_MovieAdded():
    test_service.add_movie(1,'title','description','genre')
    assert len(test_service.get_movies().get_movie_list()) == 11
    assert test_service.get_movies().get_movie_list()[10]._id == 1
    assert test_service.get_movies().get_movie_list()[10]._title == 'title'
    assert test_service.get_movies().get_movie_list()[10]._description == 'description'
    assert test_service.get_movies().get_movie_list()[10]._genre == 'genre'

def test_add_movie_InvalidInput_Error():
    try:
        test_service.add_movie('invalidID','title','description','genre')
    except:
        assert True

def test_update_movie_ValidInput_MovieUpdated():
    test_service.update_movie(1,'New Title','New Description','New Genre')
    assert test_service.get_movies().get_movie_list()[10]._title == 'New Title'
    assert test_service.get_movies().get_movie_list()[10]._description == 'New Description'
    assert test_service.get_movies().get_movie_list()[10]._genre == 'New Genre'

def test_update_movie_InvalidInput_Error():
    try:
        test_service.update_movie('invalidID','New Title','New Description','New Genre')
    except:
        assert True

def test_remove_movie_ValidInput_MovieRemoved():
    test_service.remove_movie(1)
    assert len(test_service.get_movies().get_movie_list()) == 10

def test_remove_movie_InvalidInput_Error():
    try:
        test_service.remove_movie('invalidID')
    except:
        assert True

#Client_Tests:
def test_add_client_ValidInput_ClientAdded():
    test_service.add_client(1,'Name')
    assert len(test_service.get_clients().get_client_list()) == 11
    assert test_service.get_clients().get_client_list()[10]._id == 1
    assert test_service.get_clients().get_client_list()[10]._name == 'Name'

def test_add_client_InvalidInput_Error():
    try:
        test_service.add_client('invalidID','name')
    except:
        assert True

def test_update_client_ValidInput_ClientUpdated():
    test_service.update_client(1,'New Name')
    assert test_service.get_clients().get_client_list()[10]._name == 'New Name'

def test_update_client_InvalidInput_Error():
    try:
        test_service.update_client('invalidID','New Name')
    except:
        assert True

def test_remove_client_ValidInput_ClientRemoved():
    test_service.remove_client(1)
    assert len(test_service.get_clients().get_client_list()) == 10
    
def test_remove_client_InvalidInput_Error():
    try:
        test_service.remove_client('invalidID')
    except:
        assert True