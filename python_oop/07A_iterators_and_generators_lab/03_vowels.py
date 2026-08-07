class vowels:
    def __init__(self, text: str) -> None:
        self.text = text
        self.index = 0
        self.vowels = "aeiouyAEIOUY"

    def __iter__(self) -> "vowels":
        return self

    def __next__(self) -> str:
        while self.index < len(self.text):
            current_character = self.text[self.index]
            self.index += 1

            if current_character in self.vowels:
                return current_character

        raise StopIteration