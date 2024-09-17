"""
    Generator liczb naturalnych.
    Zaślepka.

    Autor: jakiś kawalarz
"""
import random


def generate_number_between(min, max):
    #print("Losuji náhodné číslo.")
    return random.randint(min, max)


def generate_until_drawn(number, min, max):
    print("Generuji náhodná čísla, dokud nenajdu hledané číslo.")
    if number < min or number > max:
        raise ValueError
    i = 1
    while number != generate_number_between(min, max):
        i += 1
    return i
