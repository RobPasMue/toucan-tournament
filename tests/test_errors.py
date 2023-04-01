from toucan.mvp.calculator.errors import ToucanException


def test_toucan_exception():
    # Build ToucanException
    err = ToucanException("This is my exception")

    # Check it is of the correct type and check its message
    assert isinstance(err, Exception)
    assert isinstance(err, ToucanException)
    assert str(err) == "This is my exception"
