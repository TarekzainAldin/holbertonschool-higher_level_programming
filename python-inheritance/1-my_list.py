#!/user/bin/python3
"""Mylist"""


class Mylist(list):
    def print_sorted(self):
        tList = []
        for element in self.copy():
            if type(element) is int :
                tList.append(element)
                print(sorted(tList))
