# Написать итератор, который принимает список списков,
# и возвращает их плоское представление.

nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    [1, 2, None],
]

# nested_items = []

class FlatIterator:
    def __init__(self, _list):
        self.list = _list

    def __iter__(self):
        self.main_list_cursor = 0
        self.nested_list_cursor = 0
        return self

    def __next__(self):
        if self.main_list_cursor < len(self.list):
            if type(self.list[self.main_list_cursor]) == list:
                if self.nested_list_cursor < len(self.list[self.main_list_cursor]) - 1:
                    list_item = self.list[self.main_list_cursor][self.nested_list_cursor]
                    self.nested_list_cursor += 1
                    # список разбирается до предпоследнего значения, последнее выводится в else ниже,
                    # чтобы при итерации не получались лишние None
                else:
                    list_item = self.list[self.main_list_cursor][self.nested_list_cursor]
                    self.main_list_cursor += 1
                    self.nested_list_cursor = 0
            else:
                list_item = self.list[self.main_list_cursor]
                self.main_list_cursor += 1
                self.nested_list_cursor = 0
        else:
            raise StopIteration
        return list_item


if __name__ == '__main__':
    for item in FlatIterator(nested_list):
        print(item)
