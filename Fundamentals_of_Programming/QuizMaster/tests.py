from ui import Ui
from controller import Controller
from repo import Repo

test_repository=Repo()
test_controller=Controller(test_repository)
test_ui=Ui(test_controller)

class Test:
    def __init__(self):
        pass

    def run_tests(self):
        self.test_validator_add_InvalidDifficulty_RaiseException()
        self.test_validator_add_InvalidNumber_RaiseException()
        self.test_validator_add_ValidInput_NoExeptionRaised()
        self.test_validator_create_InvalidDifficulty_Exeptionraised()
        self.test_validator_create_InvalidNumber_Exeptionraised()

    def test_validator_add_InvalidDifficulty_RaiseException(self):
        try:
            test_controller.validator_add(['1','text','a','b','c','c','ez'])
        except:
            assert True
        else:
            assert False

    def test_validator_add_InvalidNumber_RaiseException(self):
        try:
            test_controller.validator_add(['C','text','a','b','c','c','easy'])
        except:
            assert True
        else:
            assert False

    def test_validator_add_ValidInput_NoExeptionRaised(self):
        try:
            test_controller.validator_add(['2','text','a','b','c','c','easy'])
        except:
            assert False
        else:
            assert True

    def test_validator_create_InvalidDifficulty_Exeptionraised(self):
        try:
            test_controller.validator_create(['har','2','quiz.txt'])
        except:
            assert True
        else:
            assert False

    def test_validator_create_InvalidNumber_Exeptionraised(self):
        try:
            test_controller.validator_create(['hard','C','quiz.txt'])
        except:
            assert True
        else:
            assert False