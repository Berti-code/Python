from repo.repository import MovieRepo,ClientRepo,RentalRepo
from service.service import Service
from ui.console import Console
from tests.tests import run_tests

run_tests()

movie_repository=MovieRepo()
client_repository=ClientRepo()
rental_repository=RentalRepo()

service=Service(movie_repository,client_repository,rental_repository)
console=Console(service)

console.run_menu()