from collections.abc import Callable
from typing import Any


def tags(
    html_tag: str
) -> Callable[[Callable[..., str]], Callable[..., str]]:

    def decorator(function: Callable[..., str]) -> Callable[..., str]:
        def wrapper(*args: Any) -> str:
            result = function(*args)

            return f"<{html_tag}>{result}</{html_tag}>"

        return wrapper

    return decorator