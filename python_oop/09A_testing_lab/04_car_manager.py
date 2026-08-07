import unittest


class CarTests(unittest.TestCase):
    def setUp(self) -> None:
        self.car = Car("BMW", "M3", 10, 60)

    def test_initialization(self) -> None:
        self.assertEqual("BMW", self.car.make)
        self.assertEqual("M3", self.car.model)
        self.assertEqual(10, self.car.fuel_consumption)
        self.assertEqual(60, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_empty_make_raises_exception(self) -> None:
        with self.assertRaises(Exception) as error:
            Car("", "M3", 10, 60)

        self.assertEqual(
            "Make cannot be null or empty!",
            str(error.exception)
        )

    def test_empty_model_raises_exception(self) -> None:
        with self.assertRaises(Exception) as error:
            Car("BMW", "", 10, 60)

        self.assertEqual(
            "Model cannot be null or empty!",
            str(error.exception)
        )

    def test_zero_fuel_consumption_raises_exception(self) -> None:
        with self.assertRaises(Exception) as error:
            Car("BMW", "M3", 0, 60)

        self.assertEqual(
            "Fuel consumption cannot be zero or negative!",
            str(error.exception)
        )

    def test_negative_fuel_consumption_raises_exception(self) -> None:
        with self.assertRaises(Exception):
            Car("BMW", "M3", -10, 60)

    def test_zero_fuel_capacity_raises_exception(self) -> None:
        with self.assertRaises(Exception) as error:
            Car("BMW", "M3", 10, 0)

        self.assertEqual(
            "Fuel capacity cannot be zero or negative!",
            str(error.exception)
        )

    def test_negative_fuel_capacity_raises_exception(self) -> None:
        with self.assertRaises(Exception):
            Car("BMW", "M3", 10, -60)

    def test_setting_negative_fuel_amount_raises_exception(self) -> None:
        with self.assertRaises(Exception) as error:
            self.car.fuel_amount = -1

        self.assertEqual(
            "Fuel amount cannot be negative!",
            str(error.exception)
        )

    def test_refuel_increases_fuel_amount(self) -> None:
        self.car.refuel(20)

        self.assertEqual(20, self.car.fuel_amount)

    def test_refuel_does_not_exceed_capacity(self) -> None:
        self.car.refuel(100)

        self.assertEqual(60, self.car.fuel_amount)

    def test_refuel_with_zero_raises_exception(self) -> None:
        with self.assertRaises(Exception) as error:
            self.car.refuel(0)

        self.assertEqual(
            "Fuel amount cannot be zero or negative!",
            str(error.exception)
        )

    def test_refuel_with_negative_value_raises_exception(self) -> None:
        with self.assertRaises(Exception):
            self.car.refuel(-10)

    def test_drive_decreases_fuel_amount(self) -> None:
        self.car.refuel(30)

        self.car.drive(100)

        self.assertEqual(20, self.car.fuel_amount)

    def test_drive_without_enough_fuel_raises_exception(self) -> None:
        self.car.refuel(5)

        with self.assertRaises(Exception) as error:
            self.car.drive(100)

        self.assertEqual(
            "You don't have enough fuel to drive!",
            str(error.exception)
        )


if __name__ == "__main__":
    unittest.main()