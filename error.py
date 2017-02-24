"""
Class: CPSC 427-02
Assignment: Assignment 3
Team Leader: Rudy Bermudez rbermudez
Developer 1: Rudy Bermudez
Developer 2: Sander Sussee
Developer 3: Ryan Rozema
Filename: error.py
Description: A recursive descent parser for logic
Note: This project is based on Lexical Analysis HW code from CPSC 326
"""


class Error(Exception):
    """ Model class of an Error
    :Parameters:
        - message: The issue that caused the error
        - line: line where error occurred
        - column: column where error occurred
    """

    def __init__(self, message):
        self.message = message

    def __str__(self):
        s = ''
        s += 'error: ' + self.message
        return s
