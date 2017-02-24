#!/usr/bin/python
"""
Class: CPSC 427-02
Assignment: Assignment 3
Team Leader: Rudy Bermudez rbermudez
Developer 1: Rudy Bermudez
Developer 2: Sander Sussee
Developer 3: Ryan Rozema
Filename: parser.py
Description: A recursive descent parser for logic
Note: This project is based on Lexical Analysis HW code from CPSC 326
"""

from mytoken import Token
from error import Error


class Parser(object):
    """ Parses Tokens and Lexemes

    :Properties:
        - lexer: The string that is converted to a token
        - tok: The instance of the token that the lexeme represents
    """

    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = None

    def __advance(self):
        """ Calls for the next token from the `lexer` and stores it to `self.current_token` """
        self.current_token = self.lexer.next_token()

    def __expect(self, token_type):
        """ Checks to see if the current token is what is syntactically expected
        :param token_type: the expected token type of type `Token`
        """
        if self.current_token == token_type:
            self.__advance()
        else:
            raise Error("was expecting a %s" % token_type)

    def parse(self):
        """
        Begins Sentence Parsing
        """
        self.__advance()
        self.__parse_sentence()
        self.__expect(Token.END)

    def __parse_sentence(self):
        if not self.current_token == Token.END:
            self.__sentence()
            self.__parse_sentence()

    def __sentence(self):
        if self.current_token == Token.NEGATION:
            self.__negation()
        elif self.current_token == Token.PROPOSITION:
            self.__proposition()
        else:
            self.__truth()

    def __negation(self):
        self.__expect(Token.NEGATION)
        self.__sentence()

    def __proposition(self):
        self.__expect(Token.PROPOSITION)
        self.__operation()

    def __truth(self):
        self.__expect(Token.TRUTH)
        self.__operation()

    def __operation(self):
        if (self.current_token == Token.NEGATION or
                self.current_token == Token.PROPOSITION or
                self.current_token == Token.TRUTH):
            raise Error("Sentences must be joined by an operation")
        elif self.current_token == Token.AND:
            self.__and()
        elif self.current_token == Token.OR:
            self.__or()
        elif self.current_token == Token.IMPLICATION:
            self.__implication()
        elif self.current_token == Token.EQUALITY:
            self.__equality()

    def __and(self):
        self.__expect(Token.AND)
        self.__sentence()

    def __or(self):
        self.__expect(Token.OR)
        self.__sentence()

    def __implication(self):
        self.__expect(Token.IMPLICATION)
        self.__sentence()

    def __equality(self):
        self.__expect(Token.EQUALITY)
        self.__sentence()
