def number_increment(numbers: list[int]) -> list[int]:
    def increase() -> list[int]:
        return [number + 1 for number in numbers]

    return increase()