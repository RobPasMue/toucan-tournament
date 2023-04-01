import pytest

from mvp.calculator.discipline import ToucanDiscipline, get_discipline_by_name
from mvp.calculator.errors import ToucanException


def test_toucan_disciplines():
    # Check the access methods to the ToucanDisciplines class
    basketball = ToucanDiscipline.BASKETBALL

    assert basketball.name == "BASKETBALL"
    assert basketball.value[0] == 0

    # Do some basic checking of the expected outputs (only types, not content)
    assert isinstance(basketball.get_pattern(), str)
    assert isinstance(basketball.get_eval_params(), dict)
    assert isinstance(basketball.get_points_in_eval_params(), tuple)


def test_get_discipline_by_name():
    # Check discipline names
    assert get_discipline_by_name("basketball") is ToucanDiscipline.BASKETBALL
    assert get_discipline_by_name("BaSkETBAll") is ToucanDiscipline.BASKETBALL
    assert get_discipline_by_name("handball") is ToucanDiscipline.HANDBALL
    assert get_discipline_by_name("HANDBALL") is ToucanDiscipline.HANDBALL

    with pytest.raises(ToucanException):
        get_discipline_by_name("mysport")
