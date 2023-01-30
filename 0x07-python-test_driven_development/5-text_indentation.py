#!/usr/bin/python3

def text_indentation(text):
    """
    This function prints a text with 2 new lines after each of these characters: ., ? and :
    If text is not a string. it will raise a TypeError.
    """
    if not isintance(text, string):
        raise TypeError("text must be a string")
    text = text.replace(".", ".\n\n")
    text = text.replace("?", "?\n\n")
    text = text.replace(":", ":\n\n")
    print(text)
