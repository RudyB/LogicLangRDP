"""
Class: CPSC 427-02
Assignment: Assignment 3
Team Leader: Rudy Bermudez rbermudez
Developer 1: Rudy Bermudez
Developer 2: Sander Sussee
Developer 3: Ryan Rozema
Filename: lexer.py
Description: A recursive descent parser for logic
Note: This project is based on Lexical Analysis HW code from CPSC 326
"""

from mytoken import Token
from error import Error


class Lexer(object):
    """ Model class of a Lexer

    :Parameters:
        - string: The sentence the user would like to analyze
    :Properties:
        - tokens: The string parameter split by a space as a delimiter
    """

    def __init__(self, string):
        # Split the sentence with a space as the delimiter
        self.tokens = string.strip().split(' ')

    def next_token(self):

        try:
            tok = self.tokens.pop(0)

            """Check for propositional symbols"""
            if len(tok) == 1 and tok.isalpha():
                return Token.PROPOSITION

            """Check for truth symbols"""
            if tok == "true" or tok == "false":
                return Token.TRUTH

            """Check for negations"""
            if tok == "not":
                return Token.NEGATION

            """Check for conjunctions"""
            if tok == "and":
                return Token.AND

            """Check for disjunctions"""
            if tok == "or":
                return Token.OR

            """Check for implications"""
            if tok == "impl":
                return Token.IMPLICATION

            """Check for equivalence symbols"""
            if tok == "=":
                return Token.EQUALITY

            # Return None if no symbol is found
            else:
                raise Error("'%s' could not be parsed" % tok)
        except IndexError:
            return Token.END