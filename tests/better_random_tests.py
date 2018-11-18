import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../SLCBInternationalHello/lib"))  # Manually import

from unittest import TestCase
from mock import (
    Mock,
    patch,
)

from better_random import (
    BetterRandom,
    GreetingPicker,
)


class GreetingPickerTests(TestCase):
    def setUp(self):
        self.custom_greetings = [
            "Well hello Mr. Fancy Pants!;",  # Army of Darkness (1992)
        ]
        self.standard_greetings = [
            "Top-o-the-morning",
        ]
        self.mock_logger = Mock()

    @patch("better_random.BetterRandom.random")
    def test_pick_type__with_custom_disabled__does_not_call_random(self, mock_random):
        picker = GreetingPicker(
            self.standard_greetings,
            self.custom_greetings,
            False,
            100,
        )

        result = picker.pick_greeting_type()
        self.assertTrue(result)
        mock_random.assert_not_called()

    @patch("better_random.BetterRandom.random")
    def test_pick_type__with_0_percent_custom__does_not_call_random(self, mock_random):
        picker = GreetingPicker(
            self.standard_greetings,
            self.custom_greetings,
            True,
            0,
        )

        result = picker.pick_greeting_type()
        self.assertTrue(result)
        mock_random.assert_not_called()

    def test_pick_type__with_100_percent_custom__picks_custom(self):
        picker = GreetingPicker(
            self.standard_greetings,
            self.custom_greetings,
            True,
            100,
            self.mock_logger,
        )
        with patch.object(BetterRandom, 'random', wraps=BetterRandom.random) as mock_random:
            result = picker.pick_greeting_type()
            self.assertFalse(result)
            mock_random.assert_called_once_with(100, self.mock_logger)
