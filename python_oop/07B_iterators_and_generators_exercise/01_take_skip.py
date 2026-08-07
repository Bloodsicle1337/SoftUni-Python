class take_skip:
    def __init__(self, step: int, count: int) -> None:
        self.step = step
        self.count = count
        self.current_number = 0
        self.current_count = 0

    def __iter__(self) -> "take_skip":
        return self

    def __next__(self) -> int:
        if self.current_count >= self.count:
            raise StopIteration

        number = self.current_number

        self.current_number += self.step
        self.current_count += 1

        return number