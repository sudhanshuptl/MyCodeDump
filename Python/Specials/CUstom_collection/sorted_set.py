

class SortedSet():
    def __init__(self, items=None):
        self._items = sorted(set(items)) if items is not None else []

    # Adding support to the container protocal that is used with 'in' or 'not in operater'
    def __contains__(self, item):
        return item in self._items

    def __len__(self):
        # this Enables uses of len function on this object
        return len(self._items)

    def __iter__(self):
        # adding iteration function
        # generator function return generator which are iterator
        for val in self._items:
            yield val

        # or shortcut return iter(self._items)

    def __getitem__(self, index):
        # adding support for sequence
        result = self._items[index]
        return SortedSet(result) if isinstance(index, slice) else result

    def __repr__(self):
        return 'SortedSet({})'.format(
            repr(self._items) if self._items else ''
        )

    def __eq__(self, other):
        if not isinstance(other, SortedSet):
            return NotImplemented
        return self._items == other._items