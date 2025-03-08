def even_if_possitive(n: int) -> int:
    """
    Return 2 if n is possitive, 1 if n is negative and 0 if n is zero.

    >>> even_if_possitive(5)
    2
    >>> even_if_possitive(-5)
    1
    >>> even_if_possitive(0)
    0
    """
    if n > 0:
        return 2

    if n < 0:
        return 1

    return 0


if __name__ == "__main__":
    # Needed if running without -m doctest
    import doctest
    doctest.testmod()
