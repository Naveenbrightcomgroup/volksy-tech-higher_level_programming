#!/usr/bin/python3
"""
This is the Mylist module.
This module contains the MyList class
"""


class MyList(list):
    """
    This is the MyList class that inherits from list
    """
    def print_sorted(self):
        """
        prints out a sorted list of ints sorted
        """
        print(sorted(self))
