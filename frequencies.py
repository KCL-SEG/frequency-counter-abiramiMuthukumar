"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    items = [str(item) for item in items]

    while len(items) > 0:
        # get first element, count how many times it's in the items list using count(), then remove it from items
        target_element = items[0]
        frequencies[target_element] = items.count(target_element)
        items = [item for item in items if item!=target_element]

    return frequencies
