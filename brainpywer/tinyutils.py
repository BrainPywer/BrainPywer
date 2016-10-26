"""
Home of all the miscellaneous BrainPywer utilities that don't deserve their own files
"""


def thaw(snowflake):
    """
    Tiny function to return the unix timestamp of a snowflake

    :param snowflake: a discord snowflake (It's unique, just like you! ha.)
    :type snowflake: int
    :return: unix timestamp of the message
    :rtype: int
    """
    return ((snowflake >> 22)+1420070400000)/1000