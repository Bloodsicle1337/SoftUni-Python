import unittest


class CatTests(unittest.TestCase):
    def setUp(self) -> None:
        self.cat = Cat("Tom")

    def test_cat_size_is_increased_after_eating(self) -> None:
        initial_size = self.cat.size

        self.cat.eat()

        self.assertEqual(initial_size + 1, self.cat.size)

    def test_cat_is_fed_after_eating(self) -> None:
        self.cat.eat()

        self.assertTrue(self.cat.fed)

    def test_cat_cannot_eat_when_already_fed(self) -> None:
        self.cat.eat()

        with self.assertRaises(Exception) as error:
            self.cat.eat()

        self.assertEqual("Already fed.", str(error.exception))

    def test_cat_cannot_sleep_when_not_fed(self) -> None:
        with self.assertRaises(Exception) as error:
            self.cat.sleep()

        self.assertEqual(
            "Cannot sleep while hungry",
            str(error.exception)
        )

    def test_cat_is_not_sleepy_after_sleeping(self) -> None:
        self.cat.eat()
        self.cat.sleep()

        self.assertFalse(self.cat.sleepy)


if __name__ == "__main__":
    unittest.main()