"""
Bowling Game Implementation
A module for calculating bowling game scores.
"""


class BowlingGame:
    """Represent a ten-frame bowling game and calculate its score."""

    def __init__(self):
        """Create an empty game ready to receive rolls."""
        self.rolls = []
        self.current_roll = 0

    def roll(self, pins):
        """Record a roll and the number of pins knocked down."""
        self.rolls.append(pins)
        self.current_roll += 1

    def score(self):
        """Return the cumulative score for the rolls recorded so far."""
        total_score = 0
        roll_index = 0

        for frame_number in range(10):
            if roll_index >= len(self.rolls):
                break

            if frame_number == 9:
                total_score += sum(self.rolls[roll_index:])
                break

            if self._is_strike(roll_index):
                total_score += 10 + self._strike_bonus(roll_index)
                roll_index += 1

            elif self._is_spare(roll_index):
                total_score += 10 + self._spare_bonus(roll_index)
                roll_index += 2

            elif roll_index + 1 >= len(self.rolls):
                total_score += self.rolls[roll_index]
                break

            else:
                total_score += (
                    self.rolls[roll_index] +
                    self.rolls[roll_index + 1]
                )
                roll_index += 2

        return total_score

    def _is_strike(self, frame_index):
        """Return whether the roll at ``frame_index`` is a strike."""
        return (
            frame_index < len(self.rolls)
            and self.rolls[frame_index] == 10
        )

    def _is_spare(self, frame_index):
        """Return whether the two rolls at ``frame_index`` make a spare."""
        return (
            frame_index + 1 < len(self.rolls)
            and self.rolls[frame_index] + self.rolls[frame_index + 1] == 10
        )

    def _strike_bonus(self, frame_index):
        """Return the two bonus rolls awarded for a strike."""
        return sum(self.rolls[frame_index + 1:frame_index + 3])

    def _spare_bonus(self, frame_index):
        """Return the next roll awarded as the bonus for a spare."""
        return (
            self.rolls[frame_index + 2]
            if frame_index + 2 < len(self.rolls)
            else 0
        )