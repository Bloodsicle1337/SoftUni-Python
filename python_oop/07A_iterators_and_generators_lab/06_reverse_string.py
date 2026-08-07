from collections.abc import Generator


def reverse_text(text: str) -> Generator[str, None, None]:
    for index in range(len(text) - 1, -1, -1):
        yield text[index]