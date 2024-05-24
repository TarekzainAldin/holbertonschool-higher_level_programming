#!/usr/bin/env python3
"""Create a class named VerboseList that extends the Python list"""


class VerboseList(list):
    def append(self, item):
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        num_items = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{num_items}] items.")

    def remove(self, item):
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        item = super().pop(index)
        print(f"Popped [{item}] from the list.")
        return item
