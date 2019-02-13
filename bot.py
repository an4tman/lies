"""
bot selects the lie from any number of positional arguments
"""


def longest(*args):
    # max() takes a second argument, a key function,
    # in this case the length of the string
    return max(args, key=len)


def shortest(*args):
    # same as max() example above
    return min(args, key=len)
