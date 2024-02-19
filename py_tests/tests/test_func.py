import pytest
from contextlib import nullcontext as does_not_raise

from src.main import *

@pytest.mark.parametrize(
        'x, y, res',
        [
           (10, 2, 6),
        #    (-100, '2', -50, pytest.raises(TypeError)),
        #    (100, 0, 100, pytest.raises(ZeroDivisionError))
        ]
        )
def test_div(x, y, res):
    # with expectation:
    assert div(x, y) == res 