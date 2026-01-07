#!/usr/bin/env python3
"""VerboseList module"""

class VerboseList(list):
    """A list that prints notifications on changes"""

    def append(self, item):
        """Add item to the list and print a notification"""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Extend list with iterable and print a notification"""
        super().extend(iterable)
        print(f"Extended the list with [{len(iterable)}] items.")

    def remove(self, item):
        """Remove item from the list and print a notification"""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Pop item from the list and print a notification"""
        item = self[index]  # get the item to be popped
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
