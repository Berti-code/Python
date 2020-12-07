from services.ComplexNumber_service import Services
from ui.console import Console
from tests.functionTests import call_tests

if __name__ == "__main__":
    call_tests()
    service=Services()
    console=Console(service)
    console.run_console()