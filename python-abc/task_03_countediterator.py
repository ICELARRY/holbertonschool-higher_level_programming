#!/usr/bin/env python3
"""CountedIterator module"""

class CountedIterator:
    """Iterator that counts how many items have been iterated over."""

    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        """Return the next item and increment the counter."""
        item = next(self.iterator)  # StopIteration otomatik olarak geçer
        self.count += 1
        return item

    def get_count(self):
        """Return the number of items iterated so far."""
        return self.count
