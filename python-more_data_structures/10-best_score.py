#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        for keyes, valeur in a_dictionary.items():
            if valeur == max(a_dictionary.values()):
                return keyes
