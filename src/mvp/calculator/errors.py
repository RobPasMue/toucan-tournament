"""Module containing potential errors to be raised by the
Toucan Tournament MVP calculator library."""


class ToucanException(Exception):
    """Specific Toucan exception class."""

    def __init__(self, msg=""):
        """Constructor for ``ToucanException``.

        Parameters
        ----------
        msg : str, optional
            The message to be raised, by default "".
        """
        Exception.__init__(self, msg="")
