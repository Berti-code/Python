from ui.console import Console
from services.ComplexNumber_service import Services
from domain.entities import ComplexNumber

test_service=Services()
test_Console=Console(test_service)

def call_tests():
    add_complex_number_ValidData_AddedToList()
    get_complex_number_InvalidData_NotAddedToList()

def add_complex_number_ValidData_AddedToList():
    test_service.add_complex_number(ComplexNumber(5,6))
    test_list=test_service.get_complex_numbers()
    assert test_list[10].real_part==5
    assert test_list[10].imaginary_part==6

def get_complex_number_InvalidData_NotAddedToList():
    test_service.add_complex_number(ComplexNumber('a','b'))
    test_list=test_service.get_complex_numbers()
    assert test_list[10].real_part!='a'
    assert test_list[10].imaginary_part!='b'