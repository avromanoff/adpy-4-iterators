# Написать итератор, который принимает список списков,
# и возвращает их плоское представление.

nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    [1, 2, None],
]

nested_items = []

class FlatIterator:
    def __init__(self, _list):
        self._list = _list

    def __iter__(self):
        self.cursor = 0
        return self

    def __next__(self):
        if self.cursor < len(self._list):
            _item = self._list[self.cursor]
            self.cursor += 1
            if type(_item) == list:
                nested_items.extend(_item)
            else:
                nested_items.append(_item)
            return nested_items
        else:
            raise StopIteration


if __name__ == '__main__':
    for item in FlatIterator(nested_list):
        print(item)
