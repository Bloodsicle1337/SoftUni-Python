import unittest


class WorkerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.worker = Worker("Peter", 1000, 5)

    def test_worker_initialization(self) -> None:
        self.assertEqual("Peter", self.worker.name)
        self.assertEqual(1000, self.worker.salary)
        self.assertEqual(5, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_rest_increases_energy_by_one(self) -> None:
        initial_energy = self.worker.energy

        self.worker.rest()

        self.assertEqual(initial_energy + 1, self.worker.energy)

    def test_work_with_zero_energy_raises_exception(self) -> None:
        self.worker.energy = 0

        with self.assertRaises(Exception) as error:
            self.worker.work()

        self.assertEqual("Not enough energy.", str(error.exception))

    def test_work_with_negative_energy_raises_exception(self) -> None:
        self.worker.energy = -1

        with self.assertRaises(Exception) as error:
            self.worker.work()

        self.assertEqual("Not enough energy.", str(error.exception))

    def test_work_increases_money_by_salary(self) -> None:
        initial_money = self.worker.money

        self.worker.work()

        self.assertEqual(
            initial_money + self.worker.salary,
            self.worker.money
        )

    def test_work_decreases_energy_by_one(self) -> None:
        initial_energy = self.worker.energy

        self.worker.work()

        self.assertEqual(initial_energy - 1, self.worker.energy)

    def test_get_info_returns_correct_information(self) -> None:
        self.worker.work()

        expected_result = "Peter has saved 1000 money."

        self.assertEqual(expected_result, self.worker.get_info())


if __name__ == "__main__":
    unittest.main()