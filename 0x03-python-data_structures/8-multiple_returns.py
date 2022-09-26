#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        new = (length,  None)
    else:
        new = (length, sentence[0])

    return (new)
