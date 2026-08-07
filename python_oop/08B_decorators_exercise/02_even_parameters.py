from collections.abc import Callable
from typing import Any


def even_parameters(
    function: Callable[..., Any]
) -> Callable[..., Any]:

    def wrapper(*args: Any) -> Any:
        for argument in args:
            if not isinstance(argument, int) or argument % 2 != 0:
                return "Please use only even numbers!"

        return function(*args)

    return wrapper