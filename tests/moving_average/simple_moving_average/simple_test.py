import pytest
import simple

class TestSimple:
    def test_WhenParameterIsNotOfTypeListOrNparray_ItShouldRaiseValueError(self):
        with pytest.raises(ValueError):
            simple.calculate("")

    def test_WhenTheParameterLenIsLessThanOne_ItShouldRaiseValueError(self):
        with pytest.raises(ValueError):
            simple.calculate([])

    def test_WhenParameterIsNparray_ItShouldCalculate(self):
        result = simple.calculate([1, 2, 3, 4])
        assert result == 2.5
        assert type(result) is float
