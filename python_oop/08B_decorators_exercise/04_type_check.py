from collections.abc import Callable
from typing import Any


def type_check(
    expected_type: type
) -> Callable[[Callable[[Any], Any]], Callable[[Any], Any]]:

    def decorator(function: Callable[[Any], Any]) -> Callable[[Any], Any]:
        def wrapper(parameter: Any) -> Any:
            if not isinstance(parameter, expected_type):
                return "Bad Type"

            return function(parameter)

        return wrapper

    return decorator