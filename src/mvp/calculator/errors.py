"""Module containing errors to be raised by the Toucan Tournament MVP calculator library."""


class ToucanException(Exception):
    """Specific Toucan exception class."""

    def __init__(self, msg=""):
        """Instantiate ``ToucanException`` object.

        Parameters
        ----------
        msg : str, optional
            The message to be raised, by default "".
        """
        Exception.__init__(self, msg="")
