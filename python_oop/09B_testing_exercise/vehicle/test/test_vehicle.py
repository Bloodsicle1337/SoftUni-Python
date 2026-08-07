import unittest

from project.vehicle import Vehicle


class VehicleTests(unittest.TestCase):
    def setUp(self) -> None:
        self.vehicle = Vehicle(100, 150)

    def test_initialization_sets_correct_attributes(self) -> None:
        self.assertEqual(100, self.vehicle.fuel)
        self.assertEqual(100, self.vehicle.capacity)
        self.assertEqual(150, self.vehicle.horse_power)
        self.assertEqual(
            Vehicle.DEFAULT_FUEL_CONSUMPTION,
            self.vehicle.fuel_consumption
        )

    def test_default_fuel_consumption_is_correct(self) -> None:
        self.assertEqual(1.25, Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_drive_decreases_fuel_correctly(self) -> None:
        self.vehicle.drive(20)

        expected_fuel = 100 - 20 * 1.25

        self.assertEqual(expected_fuel, self.vehicle.fuel)

    def test_drive_with_exact_amount_of_fuel(self) -> None:
        vehicle = Vehicle(25, 150)

        vehicle.drive(20)

        self.assertEqual(0, vehicle.fuel)

    def test_drive_without_enough_fuel_raises_exception(self) -> None:
        with self.assertRaises(Exception) as error:
            self.vehicle.drive(100)

        self.assertEqual("Not enough fuel", str(error.exception))

    def test_failed_drive_does_not_change_fuel(self) -> None:
        initial_fuel = self.vehicle.fuel

        with self.assertRaises(Exception):
            self.vehicle.drive(100)

        self.assertEqual(initial_fuel, self.vehicle.fuel)

    def test_refuel_increases_fuel_correctly(self) -> None:
        self.vehicle.drive(20)

        self.vehicle.refuel(10)

        self.assertEqual(85, self.vehicle.fuel)

    def test_refuel_to_full_capacity(self) -> None:
        self.vehicle.drive(20)

        self.vehicle.refuel(25)

        self.assertEqual(self.vehicle.capacity, self.vehicle.fuel)

    def test_refuel_above_capacity_raises_exception(self) -> None:
        self.vehicle.drive(20)

        with self.assertRaises(Exception) as error:
            self.vehicle.refuel(26)

        self.assertEqual("Too much fuel", str(error.exception))

    def test_failed_refuel_does_not_change_fuel(self) -> None:
        self.vehicle.drive(20)
        initial_fuel = self.vehicle.fuel

        with self.assertRaises(Exception):
            self.vehicle.refuel(26)

        self.assertEqual(initial_fuel, self.vehicle.fuel)

    def test_str_returns_correct_information(self) -> None:
        expected_result = (
            "The vehicle has 150 horse power with 100 fuel left "
            "and 1.25 fuel consumption"
        )

        self.assertEqual(expected_result, str(self.vehicle))


if __name__ == "__main__":
    unittest.main()