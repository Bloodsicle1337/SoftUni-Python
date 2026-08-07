class dictionary_iter:
    def __init__(self, dictionary: dict) -> None:
        self.items = list(dictionary.items())
        self.index = 0

    def __iter__(self) -> "dictionary_iter":
        return self

    def __next__(self) -> tuple:
        if self.index >= len(self.items):
            raise StopIteration

        current_item = self.items[self.index]
        self.index += 1

        return current_item