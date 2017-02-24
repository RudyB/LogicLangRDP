#!/usr/bin/python
"""
Class: CPSC 427-02
Assignment: Assignment 3
Team Leader: Rudy Bermudez rbermudez
Developer 1: Sander Sussee
Developer 2: Ryan Rozema
Filename: main.py
Description: A recursive descent parser for logic
Note: This project is based on Lexical Analysis HW code from CPSC 326
"""

from parser import Parser
from lexer import Lexer
from error import Error

grammar = """
Valid Grammar

# SENTENCE : PROP | TRUTH | NEG | AND | OR | IMPL | EQ
# PROPOSITION : a | b | c | ... | z
# TRUTH : true | false
# NEGATION : not S
# AND : S and S
# OR : S or S
# IMPLICATION : S impl S
# EQUALITY : S = S

"""

prompt = """
Enter "grammar" to see the language grammar
Enter "end" to quit.

Enter a logical statement as a string to begin parsing

"""

run = True
print (grammar)

while run:
    try:
        isCorrect = True
        user_input = raw_input(prompt)
        if user_input == "end":
            break
        lexer = Lexer(user_input)
        parser = Parser(lexer)
        parser.parse()
    except Error:
        isCorrect = False
    if isCorrect:
        print "\nAnswer: yes\n"
    else:
        print "\nAnswer: no\n"



