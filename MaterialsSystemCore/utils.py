

def validate_integer(number: str) -> bool:
    """Returns False if number is a negative or a non int value
    :param number: the number to validate."""

    return number.isnumeric()
