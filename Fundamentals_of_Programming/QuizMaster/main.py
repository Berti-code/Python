from ui import Ui
from controller import Controller
from repo import Repo
from tests import Test

repository=Repo()
controller=Controller(repository)
ui=Ui(controller)

test_object=Test()
test_object.run_tests()

ui.run_app()