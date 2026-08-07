class countdown_iterator:
    def __init__(self, count: int) -> None:
        self.current_number = count

    def __iter__(self) -> "countdown_iterator":
        return self

    def __next__(self) -> int:
        if self.current_number < 0:
            raise StopIteration

        number = self.current_number
        self.current_number -= 1

        return number