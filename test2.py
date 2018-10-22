#!/usr/bin/python

def formatter(text):
    return "******\n" + text + "\n******"

def printWithFormatter(formattingFunction, text):
    print(formattingFunction(text))

printWithFormatter(formatter, "hello")