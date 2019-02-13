#!/usr/bin/python3

"""
bot selects the lie from any number of positional arguments
"""

# input validation


def validate_length(us):
    """
    Check that input string is not longer than 140 characters.

    param us: a user-input string
    rtype: bool
    """
    return len(us) <= 140


def validate_sentence(us):
    """
    Check that input string ends with a period.

    param us: a user-input string
    rtype: bool
    """
    return us[-1] == '.'


def longest(*args):
    """
    Return the argument that is the longest input string.

    max() takes a second argument, a key function,
    in this case the length of the string

    param *args: an array of user-input strings gathered from command line
    rtype: string
    """
    return max(args, key=len)


def shortest(*args):
    """
    Return the argument that is the shortest input string.

    min() takes a second argument, a key function,
    in this case the length of the string

    param *args: an array of user-input strings gathered from command line
    rtype: string
    """
    return min(args, key=len)
