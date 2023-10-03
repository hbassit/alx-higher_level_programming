#!/usr/bin/python3
"""This module contains one function for printing text in specific format"""


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
