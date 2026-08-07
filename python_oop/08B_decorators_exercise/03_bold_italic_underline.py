from collections.abc import Callable
from typing import Any


def make_bold(function: Callable[..., str]) -> Callable[..., str]:
    def wrapper(*args: Any) -> str:
        result = function(*args)

        return f"<b>{result}</b>"

    return wrapper


def make_italic(function: Callable[..., str]) -> Callable[..., str]:
    def wrapper(*args: Any) -> str:
        result = function(*args)

        return f"<i>{result}</i>"

    return wrapper


def make_underline(function: Callable[..., str]) -> Callable[..., str]:
    def wrapper(*args: Any) -> str:
        result = function(*args)

        return f"<u>{result}</u>"

    return wrapper