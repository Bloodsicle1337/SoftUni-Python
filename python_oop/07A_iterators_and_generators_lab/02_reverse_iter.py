class reverse_iter:
    def __init__(self, iterable: list) -> None:
        self.iterable = iterable
        self.index = len(iterable) - 1

    def __iter__(self) -> "reverse_iter":
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration

        current_item = self.iterable[self.index]
        self.index -= 1

        return current_item