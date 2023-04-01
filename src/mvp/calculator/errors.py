"""Module containing potential errors to be raised by the
Tucan Tournament MVP calculator library."""

class TucanException(Exception):
    """Specific Tucan exception class."""
    
    def __init__(self, msg=""):
        """Constructor for ``TucanException``.

        Parameters
        ----------
        msg : str, optional
            The message to be raised, by default "".
        """
        Exception.__init__(self, msg="")