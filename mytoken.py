"""
Class: CPSC 427-02
Assignment: Assignment 3
Team Leader: Rudy Bermudez rbermudez
Developer 1: Rudy Bermudez
Developer 2: Sander Sussee
Developer 3: Ryan Rozema
Filename: mytoken.py
Description: A recursive descent parser for logic
Note: This project is based on Lexical Analysis HW code from CPSC 326
"""


class Token(object):
    PROPOSITION = "PROPOSITION"
    TRUTH = "TRUTH"
    NEGATION = "NEGATION"
    AND = "AND"
    OR = "OR"
    IMPLICATION = "IMPLICATION"
    EQUALITY = "EQUALITY"
    END = "END"
