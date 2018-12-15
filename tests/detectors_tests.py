import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../SLCBInternationalHello/lib"))  # Manually import

from unittest import TestCase
from mock import MagicMock

from constants import ScriptConstants
from detectors import GreetingDetector


class GreetingDetectorTests(TestCase):
    def setUp(self):
        self.greetings = []
        for greeting in ScriptConstants.DEFAULT_GREETINGS:
            lower_greeting = greeting.lower()
            self.greetings.append(lower_greeting)

        self.detector = GreetingDetector(
            standard_greetings=self.greetings,
            custom_greetings=[],
            custom_enabled=False
        )

    def test_constructor__builds_lookup_table(self):
        self.assertEqual(len(self.detector.greetings_lookup[1]), 41)
        self.assertEqual(len(self.detector.greetings_lookup[2]), 10)
        self.assertListEqual(self.detector.greetings_lookup.keys(), [1, 2])

    def test_is_greeting__one_word_greeting__returns_true(self):
        mock_data = MagicMock()
        mock_data.GetParamCount.return_value = 1
        mock_data.GetParam.return_value = "Top-o-the-morning"
        self.assertTrue(self.detector.is_greeting(mock_data))

    def test_is_greeting__one_word_unicode_greeting__returns_true(self):
        mock_data = MagicMock()
        mock_data.GetParamCount.return_value = 1
        mock_data.GetParam.return_value = u'\u0645\u0631\u062d\u0628\u0627'  # Arabic - marhabaan
        self.assertTrue(self.detector.is_greeting(mock_data))

    def test_is_greeting__two_word_greeting__returns_true(self):
        mock_data = MagicMock()
        mock_data.GetParamCount.return_value = 2
        mock_data.GetParam.side_effect = ["Dia", "Dia", "Dhuit"] # Polish
        result = self.detector.is_greeting(mock_data)
        self.assertTrue(result)

    def test_is_greeting__two_word_unicode_greeting__returns_true(self):
        mock_data = MagicMock()
        mock_data.GetParamCount.return_value = 2
        mock_data.GetParam.side_effect = [u'Dzie\u0144', u'Dzie\u0144', "Dobry"]  # Polish
        result = self.detector.is_greeting(mock_data)
        self.assertTrue(result)

    def test_is_greeting__multi_word_not_a_greeting__returns_false(self):
        mock_data = MagicMock()
        mock_data.GetParamCount.return_value = 3
        # The input will be "rogukalth lord psyc0n"
        mock_data.GetParam.side_effect = ["rogukalth", "rogukalth", "lord", "rogukalth", "lord", "psyc0n"]
        result = self.detector.is_greeting(mock_data)
        self.assertFalse(result)

    def test_is_greeting_one_word_not_a_greeting__returns_false(self):
        # Test that it does not overloop and try to look for 2 word greetings
        # If this loops more than expected, it will throw a Mock Iterator type exception
        mock_data = MagicMock()
        mock_data.GetParamCount.return_value = 1
        mock_data.GetParam.side_effect = ["rydogg1391"]
        result = self.detector.is_greeting(mock_data)
        self.assertFalse(result)
