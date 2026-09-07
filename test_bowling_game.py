"""Unit tests for the bowling game scoring implementation."""

import unittest
from bowling_game import BowlingGame


class TestBowlingGame(unittest.TestCase):
    """Unit tests for the BowlingGame class."""

    def test_gutter_game(self):
        """A game with all gutter balls should score 0."""
        game = BowlingGame()

        for _ in range(20):
            game.roll(0)

        self.assertEqual(game.score(), 0)

    def test_regular_game(self):
        """A regular game with no strikes or spares should score correctly."""
        game = BowlingGame()

        rolls = [
            3, 4,
            2, 5,
            1, 6,
            4, 2,
            8, 1,
            7, 1,
            5, 3,
            2, 3,
            4, 3,
            2, 6
        ]

        for pins in rolls:
            game.roll(pins)

        self.assertEqual(game.score(), 72)

    def test_spare(self):
        """A spare should score 10 plus the next roll."""
        game = BowlingGame()

        rolls = [
            5, 5,
            4, 3,
            0, 0,
            0, 0,
            0, 0,
            0, 0,
            0, 0,
            0, 0,
            0, 0,
            0, 0
        ]

        for pins in rolls:
            game.roll(pins)

        self.assertEqual(game.score(), 21)

    def test_strike(self):
        """A strike should score 10 plus the next two rolls."""
        game = BowlingGame()

        rolls = [
            10,
            3, 6,
            0, 0,
            0, 0,
            0, 0,
            0, 0,
            0, 0,
            0, 0,
            0, 0,
            0, 0
        ]

        for pins in rolls:
            game.roll(pins)

        self.assertEqual(game.score(), 28)

    def test_consecutive_strikes(self):
        """Consecutive strikes should receive the correct bonuses."""
        game = BowlingGame()

        rolls = [
            10,
            10,
            4, 2,
            0, 0,
            0, 0,
            0, 0,
            0, 0,
            0, 0,
            0, 0,
            0, 0
        ]

        for pins in rolls:
            game.roll(pins)

        self.assertEqual(game.score(), 46)

    def test_all_spares(self):
        """Ten frames of 5 + 5 followed by a 5 should score 150."""
        game = BowlingGame()

        for _ in range(21):
            game.roll(5)

        self.assertEqual(game.score(), 150)

    def test_perfect_game(self):
        """A perfect game of 12 strikes should score 300."""
        game = BowlingGame()

        for _ in range(12):
            game.roll(10)

        self.assertEqual(game.score(), 300)

    def test_tenth_frame_strike(self):
        """A tenth-frame strike should include its two bonus rolls."""
        game = BowlingGame()

        rolls = [
            0, 0,
            0, 0,
            0, 0,
            0, 0,
            0, 0,
            0, 0,
            0, 0,
            0, 0,
            0, 0,
            10, 10, 8
        ]

        for pins in rolls:
            game.roll(pins)

        self.assertEqual(game.score(), 28)

    def test_tenth_frame_spare(self):
        """A tenth-frame spare should include one bonus roll."""
        game = BowlingGame()

        rolls = [
            0, 0,
            0, 0,
            0, 0,
            0, 0,
            0, 0,
            0, 0,
            0, 0,
            0, 0,
            0, 0,
            7, 3, 5
        ]

        for pins in rolls:
            game.roll(pins)

        self.assertEqual(game.score(), 15)

    # ---------------------------------------------------------
    # ADDITIONAL TESTS
    # ---------------------------------------------------------

    def test_boundary_ten(self):
        """Ten pins is the maximum valid score for one roll."""
        game = BowlingGame()

        rolls = [
            10,
            0, 0,
            0, 0,
            0, 0,
            0, 0,
            0, 0,
            0, 0,
            0, 0,
            0, 0,
            0, 0
        ]

        for pins in rolls:
            game.roll(pins)

        self.assertEqual(game.score(), 10)

    def test_spare_followed_by_strike(self):
        """A spare followed by a strike should receive the correct bonus."""
        game = BowlingGame()

        rolls = [
            5, 5,
            10,
            4, 3,
            0, 0,
            0, 0,
            0, 0,
            0, 0,
            0, 0,
            0, 0
        ]

        for pins in rolls:
            game.roll(pins)

        self.assertEqual(game.score(), 44)

    def test_strike_followed_by_spare(self):
        """A strike followed by a spare should receive the correct bonuses."""
        game = BowlingGame()

        rolls = [
            10,
            5, 5,
            4, 3,
            0, 0,
            0, 0,
            0, 0,
            0, 0,
            0, 0,
            0, 0
        ]

        for pins in rolls:
            game.roll(pins)

        self.assertEqual(game.score(), 41)

    def test_several_consecutive_strikes(self):
        """Several consecutive strikes should calculate bonuses correctly."""
        game = BowlingGame()

        rolls = [
            10,
            10,
            10,
            4, 3,
            0, 0,
            0, 0,
            0, 0,
            0, 0,
            0, 0,
            0, 0
        ]

        for pins in rolls:
            game.roll(pins)

        self.assertEqual(game.score(), 78)


if __name__ == "__main__":
    unittest.main()