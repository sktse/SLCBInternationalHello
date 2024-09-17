import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../SLCBInternationalHello/lib"))  # Manually import

from unittest import TestCase

from parsers import (
    InputParser,
    SemicolonSeparatedParser,
    NewLineSeparatedFileParser,
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


class NewLineSeparatedFileParserTest(TestCase):
    def setUp(self):
        file_path = os.path.join(os.path.join(os.path.dirname(__file__), "settings_files", "taken-read.txt"))
        self.parser = NewLineSeparatedFileParser(file_path=file_path)

    def test_read(self):
        result = self.parser.read()

        expected_result = [
            "I don't know who you are.",
            "I don't know what you want.",
            "If you are looking for ransom I can tell you I don't have money,",
            "but what I do have are a very particular set of skills.",
            "Skills I have acquired over a very long career.",
            "Skills that make me a nightmare for people like you.",
            "If you let my daughter go now that'll be the end of it.",
            "I will not look for you,",
            "I will not pursue you,",
            "but if you don't,",
            "I will look for you,",
            "I will find you and I will kill you.",
            "-- Liam Neeson, Taken",
        ]
        self.assertListEqual(result, expected_result)

    def test_write(self):
        self.parser.file_path = os.path.join(os.path.join(os.path.dirname(__file__), "settings_files", "taken-write.txt"))
        lines = [
            "You know, we used to outsource this kind of thing.",
            "But what we found was the countries we outsourced to had unreliable power grids.",
            "Very Third World.",
            "You'd turn on a switch - power wouldn't come on, and then tempers would get short.",
            "People would resort to pulling fingernails.",
            "Acid drips on bare skin.",
            "The whole exercise would become counterproductive.",
            "But here, the power's stable.",
            "Here, there's a nice even flow.",
            "Here, you can flip a switch and the power stays on all day.",
            "Where is she?",
        ]
        self.parser.write(lines)

        result = self.parser.read()
        self.assertListEqual(result, lines)

