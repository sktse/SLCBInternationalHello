import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../SLCBInternationalHello/lib"))  # Manually import

from unittest import TestCase

from parsers import (
    InputParser,
    SemicolonSeparatedParser,
)


class InputParserTests(TestCase):
    def test_no_trailing_anything__returns_lower(self):
        result = InputParser.parse("Carpe dentum. Seize the teeth")
        self.assertEqual(result, "carpe dentum. seize the teeth")

    def test_trailing_punctuation__returns_lower_and_no_trailing_punctuation(self):
        result = InputParser.parse("Oh, as I hold this cold meat, I'm reminded of Winston!")
        self.assertEqual(result, "oh, as i hold this cold meat, i'm reminded of winston")

    def test_trailing_whitespace__returns_lower_and_trimmed(self):
        result = InputParser.parse("Look, Nattie. That's called liposuction              ")
        self.assertEqual(result, "look, nattie. that's called liposuction")

    def test_trailing_whitespace_after_punctuation__returns_lower_and_trimmed(self):
        result = InputParser.parse("I must look like a yeti in this getup              !")
        self.assertEqual(result, "i must look like a yeti in this getup")


class SemicolonSeparatedParserTests(TestCase):
    def test_semicolon_string(self):
        result = SemicolonSeparatedParser.parse("!hello;morning;evening")
        self.assertListEqual(result, ["!hello", "morning", "evening"])

    def test_semicolon_string_with_whitespace(self):
        result = SemicolonSeparatedParser.parse("!hello          ;morning;        evening")
        self.assertListEqual(result, ["!hello", "morning", "evening"])

    def test_semicolon_string_with_empty_semicolons(self):
        result = SemicolonSeparatedParser.parse("!hello  ;;morning;     ;;;;evening")
        self.assertListEqual(result, ["!hello", "morning", "evening"])

    def test_with_no_semicolons(self):
        result = SemicolonSeparatedParser.parse("I'm melting like a snow cone in Phoenix.")
        self.assertListEqual(result, ["I'm melting like a snow cone in Phoenix."])
