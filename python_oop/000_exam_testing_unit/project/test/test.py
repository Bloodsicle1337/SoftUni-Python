import unittest
from project.legendary_item import LegendaryItem

class TestLegendaryItem(unittest.TestCase):
    def setUp(self):
        self.item = LegendaryItem("Sword-1", 50, 50, 100)

    def test_init(self):
        self.assertEqual("Sword-1", self.item.identifier)
        self.assertEqual(50, self.item.power)
        self.assertEqual(50, self.item.durability)
        self.assertEqual(100, self.item.price)

    def test_identifier_raises_when_contains_invalid_characters(self):
        with self.assertRaises(ValueError) as error:
            LegendaryItem("Sword!", 50, 50, 100)

        self.assertEqual(
            "Identifier can only contain letters, digits, or hyphens!",
            str(error.exception)
        )

    def test_identifier_raises_when_less_than_four_characters(self):
        with self.assertRaises(ValueError) as error:
            LegendaryItem("Ab1", 50, 50, 100)

        self.assertEqual(
            "Identifier must be at least 4 characters long!",
            str(error.exception)
        )

    def test_power_raises_when_negative(self):
        with self.assertRaises(ValueError) as error:
            LegendaryItem("Sword", -1, 50, 100)

        self.assertEqual(
            "Power must be a non-negative integer!",
            str(error.exception)
        )

    def test_durability_raises_when_less_than_one(self):
        with self.assertRaises(ValueError) as error:
            LegendaryItem("Sword", 50, 0, 100)

        self.assertEqual(
            "Durability must be between 1 and 100 inclusive!",
            str(error.exception)
        )

    def test_durability_raises_when_more_than_100(self):
        with self.assertRaises(ValueError) as error:
            LegendaryItem("Sword", 50, 101, 100)

        self.assertEqual(
            "Durability must be between 1 and 100 inclusive!",
            str(error.exception)
        )

    def test_price_raises_when_zero(self):
        with self.assertRaises(ValueError) as error:
            LegendaryItem("Sword", 50, 50, 0)

        self.assertEqual(
            "Price must be a multiple of 10 and not 0!",
            str(error.exception)
        )

    def test_price_raises_when_not_multiple_of_10(self):
        with self.assertRaises(ValueError) as error:
            LegendaryItem("Sword", 50, 50, 105)

        self.assertEqual(
            "Price must be a multiple of 10 and not 0!",
            str(error.exception)
        )

    def test_is_precious_returns_true(self):
        self.assertTrue(self.item.is_precious)

    def test_is_precious_returns_false(self):
        item = LegendaryItem("Sword", 49, 50, 100)

        self.assertFalse(item.is_precious)

    def test_enhance(self):
        self.item.enhance()

        self.assertEqual(100, self.item.power)
        self.assertEqual(60, self.item.durability)
        self.assertEqual(110, self.item.price)

    def test_enhance_does_not_increase_durability_above_100(self):
        item = LegendaryItem("Sword", 50, 95, 100)

        item.enhance()

        self.assertEqual(100, item.durability)

    def test_evaluate_returns_eligible(self):
        result = self.item.evaluate(40)

        self.assertEqual("Sword-1 is eligible.", result)

    def test_evaluate_returns_not_eligible_when_power_is_low(self):
        item = LegendaryItem("Sword", 40, 50, 100)

        result = item.evaluate(40)

        self.assertEqual("Item not eligible.", result)

    def test_evaluate_returns_not_eligible_when_durability_is_low(self):
        result = self.item.evaluate(60)

        self.assertEqual("Item not eligible.", result)

if __name__ == "__main__":
    unittest.main()