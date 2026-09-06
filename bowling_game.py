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
        score = 0
        frame_index = 0

        for frame in range(10):
            if frame_index >= len(self.rolls):
                break

            if frame == 9:
                score += sum(self.rolls[frame_index:])
                break

            if self._is_strike(frame_index):
                score += 10 + self._strike_bonus(frame_index)
                frame_index += 1
            elif self._is_spare(frame_index):
                score += 10 + self._spare_bonus(frame_index)
                frame_index += 2
            else:
                score += self.rolls[frame_index] + self.rolls[frame_index + 1]
                frame_index += 2

        return score

    def _is_strike(self, frame_index):
        """Return whether the roll at ``frame_index`` is a strike."""
        return frame_index < len(self.rolls) and self.rolls[frame_index] == 10

    def _is_spare(self, frame_index):
        """Return whether the two rolls at ``frame_index`` make a spare."""
        return frame_index + 1 < len(self.rolls) and self.rolls[frame_index] + self.rolls[frame_index + 1] == 10

    def _strike_bonus(self, frame_index):
        """Return the two bonus rolls awarded for a strike."""
        return self.rolls[frame_index + 1] + self.rolls[frame_index + 2]

    def _spare_bonus(self, frame_index):
        """Return the next roll awarded as the bonus for a spare."""
        return self.rolls[frame_index + 2]