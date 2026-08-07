import unittest

from project.mammal import Mammal


class MammalTests(unittest.TestCase):
    def setUp(self) -> None:
        self.mammal = Mammal("Dog", "Domestic", "Woof")

    def test_initialization_sets_correct_attributes(self) -> None:
        self.assertEqual("Dog", self.mammal.name)
        self.assertEqual("Domestic", self.mammal.type)
        self.assertEqual("Woof", self.mammal.sound)

    def test_make_sound_returns_correct_message(self) -> None:
        expected_result = "Dog makes Woof"

        self.assertEqual(expected_result, self.mammal.make_sound())

    def test_get_kingdom_returns_animals(self) -> None:
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_info_returns_correct_message(self) -> None:
        expected_result = "Dog is of type Domestic"

        self.assertEqual(expected_result, self.mammal.info())


if __name__ == "__main__":
    unittest.main()