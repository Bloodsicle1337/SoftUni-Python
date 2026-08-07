import unittest

from project.hero import Hero


class HeroTests(unittest.TestCase):
    def setUp(self) -> None:
        self.hero = Hero("Peter", 2, 100, 20)
        self.enemy = Hero("George", 1, 80, 10)

    def test_initialization_sets_correct_attributes(self) -> None:
        self.assertEqual("Peter", self.hero.username)
        self.assertEqual(2, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(20, self.hero.damage)

    def test_battle_against_same_username_raises_exception(self) -> None:
        enemy = Hero("Peter", 3, 100, 20)

        with self.assertRaises(Exception) as error:
            self.hero.battle(enemy)

        self.assertEqual(
            "You cannot fight yourself",
            str(error.exception)
        )

    def test_battle_when_hero_has_zero_health_raises_value_error(self) -> None:
        self.hero.health = 0

        with self.assertRaises(ValueError) as error:
            self.hero.battle(self.enemy)

        self.assertEqual(
            "Your health is lower than or equal to 0. You need to rest",
            str(error.exception)
        )

    def test_battle_when_hero_has_negative_health_raises_value_error(
        self
    ) -> None:
        self.hero.health = -10

        with self.assertRaises(ValueError):
            self.hero.battle(self.enemy)

    def test_battle_when_enemy_has_zero_health_raises_value_error(
        self
    ) -> None:
        self.enemy.health = 0

        with self.assertRaises(ValueError) as error:
            self.hero.battle(self.enemy)

        self.assertEqual(
            "You cannot fight George. He needs to rest",
            str(error.exception)
        )

    def test_battle_when_enemy_has_negative_health_raises_value_error(
        self
    ) -> None:
        self.enemy.health = -10

        with self.assertRaises(ValueError):
            self.hero.battle(self.enemy)

    def test_battle_when_both_heroes_die_returns_draw(self) -> None:
        hero = Hero("Peter", 1, 10, 10)
        enemy = Hero("George", 1, 10, 10)

        result = hero.battle(enemy)

        self.assertEqual("Draw", result)
        self.assertEqual(0, hero.health)
        self.assertEqual(0, enemy.health)

    def test_battle_when_hero_wins(self) -> None:
        hero = Hero("Peter", 2, 100, 30)
        enemy = Hero("George", 1, 50, 10)

        result = hero.battle(enemy)

        self.assertEqual("You win", result)
        self.assertEqual(3, hero.level)
        self.assertEqual(95, hero.health)
        self.assertEqual(35, hero.damage)
        self.assertEqual(-10, enemy.health)

    def test_battle_when_hero_loses(self) -> None:
        hero = Hero("Peter", 1, 20, 5)
        enemy = Hero("George", 2, 100, 20)

        result = hero.battle(enemy)

        self.assertEqual("You lose", result)
        self.assertEqual(-20, hero.health)
        self.assertEqual(3, enemy.level)
        self.assertEqual(100, enemy.health)
        self.assertEqual(25, enemy.damage)

    def test_battle_when_both_survive_upgrades_enemy(self) -> None:
        result = self.hero.battle(self.enemy)

        self.assertEqual("You lose", result)
        self.assertEqual(90, self.hero.health)
        self.assertEqual(2, self.enemy.level)
        self.assertEqual(45, self.enemy.health)
        self.assertEqual(15, self.enemy.damage)

    def test_str_returns_correct_information(self) -> None:
        expected_result = (
            "Hero Peter: 2 lvl\n"
            "Health: 100\n"
            "Damage: 20\n"
        )

        self.assertEqual(expected_result, str(self.hero))


if __name__ == "__main__":
    unittest.main()