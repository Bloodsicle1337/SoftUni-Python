import unittest


class IntegerListTests(unittest.TestCase):
    def setUp(self) -> None:
        self.integer_list = IntegerList(1, 2, 3)

    def test_initialization_stores_only_integers(self) -> None:
        integer_list = IntegerList(1, "two", 3.5, 4, None)

        self.assertEqual([1, 4], integer_list.get_data())

    def test_add_integer_adds_it_and_returns_data(self) -> None:
        result = self.integer_list.add(4)

        self.assertEqual([1, 2, 3, 4], result)

    def test_add_non_integer_raises_value_error(self) -> None:
        with self.assertRaises(ValueError):
            self.integer_list.add("four")

    def test_remove_index_returns_removed_element(self) -> None:
        result = self.integer_list.remove_index(1)

        self.assertEqual(2, result)
        self.assertEqual([1, 3], self.integer_list.get_data())

    def test_remove_invalid_index_raises_index_error(self) -> None:
        with self.assertRaises(IndexError):
            self.integer_list.remove_index(3)

    def test_get_returns_element(self) -> None:
        self.assertEqual(2, self.integer_list.get(1))

    def test_get_invalid_index_raises_index_error(self) -> None:
        with self.assertRaises(IndexError):
            self.integer_list.get(3)

    def test_insert_adds_element_at_index(self) -> None:
        self.integer_list.insert(1, 10)

        self.assertEqual([1, 10, 2, 3], self.integer_list.get_data())

    def test_insert_invalid_index_raises_index_error(self) -> None:
        with self.assertRaises(IndexError):
            self.integer_list.insert(3, 10)

    def test_insert_non_integer_raises_value_error(self) -> None:
        with self.assertRaises(ValueError):
            self.integer_list.insert(1, "ten")

    def test_get_biggest_returns_biggest_number(self) -> None:
        integer_list = IntegerList(4, 12, -3, 8)

        self.assertEqual(12, integer_list.get_biggest())

    def test_get_index_returns_correct_index(self) -> None:
        self.assertEqual(1, self.integer_list.get_index(2))


if __name__ == "__main__":
    unittest.main()