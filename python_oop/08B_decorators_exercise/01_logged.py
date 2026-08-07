from collections.abc import Callable
from typing import Any


def logged(function: Callable[..., Any]) -> Callable[..., str]:
    def wrapper(*args: Any) -> str:
        result = function(*args)
        arguments = ", ".join(str(argument) for argument in args)

        return (
            f"you called {function.__name__}({arguments})\n"
            f"it returned {result}"
        )

    return wrapper