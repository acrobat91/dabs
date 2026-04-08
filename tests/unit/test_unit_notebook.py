from runtime.nutterfixture import NutterFixture
from src.notebook import add_numbers

class TestAddNumbers(NutterFixture):

    def assertion_add(self):
        result = add_numbers(2, 3)
        assert result == 5, f"Expected 5 but got {result}"