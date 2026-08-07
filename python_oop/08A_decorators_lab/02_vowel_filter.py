from collections.abc import Callable


def vowel_filter(
    function: Callable[[], list[str]]
) -> Callable[[], list[str]]:

    def wrapper() -> list[str]:
        letters = function()
        vowels = "aeiouyAEIOUY"

        return [letter for letter in letters if letter in vowels]

    return wrapper