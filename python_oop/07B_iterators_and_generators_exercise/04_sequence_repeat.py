class sequence_repeat:
    def __init__(self, sequence: str, number: int) -> None:
        self.sequence = sequence
        self.number = number
        self.index = 0

    def __iter__(self) -> "sequence_repeat":
        return self

    def __next__(self) -> str:
        if self.index >= self.number:
            raise StopIteration

        current_item = self.sequence[self.index % len(self.sequence)]
        self.index += 1

        return current_item