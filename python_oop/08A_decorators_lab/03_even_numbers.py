from collections.abc import Callable


def even_numbers(
    function: Callable[[list[int]], list[int]]
) -> Callable[[list[int]], list[int]]:

    def wrapper(numbers: list[int]) -> list[int]:
        result = function(numbers)

        return [number for number in result if number % 2 == 0]

    return wrapper