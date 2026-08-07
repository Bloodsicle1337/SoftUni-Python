from collections.abc import Callable


def multiply(
    times: int
) -> Callable[
    [Callable[[int], int]],
    Callable[[int], int]
]:

    def decorator(
        function: Callable[[int], int]
    ) -> Callable[[int], int]:

        def wrapper(number: int) -> int:
            result = function(number)

            return result * times

        return wrapper

    return decorator