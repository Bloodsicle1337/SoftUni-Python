from collections.abc import Callable


def cache(function: Callable[[int], int]) -> Callable[[int], int]:
    log = {}

    def wrapper(number: int) -> int:
        if number not in log:
            log[number] = function(number)

        return log[number]

    wrapper.log = log

    return wrapper


@cache
def fibonacci(number: int) -> int:
    if number < 2:
        return number

    return fibonacci(number - 1) + fibonacci(number - 2)