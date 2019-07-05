import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../SLCBInternationalHello/lib"))  # Manually import

from unittest import TestCase
from mock import Mock

from settings import (
    CustomOutputSettings,
    ScriptSettings,
)


class ScriptSettingsTests(TestCase):
    def test_default_constructor__setups_default_values(self):
        settings = ScriptSettings()
        self.assertEqual(settings.Permission, "everyone")
        self.assertEqual(settings.Info, "")
        self.assertEqual(settings.Cooldown, 60)
        self.assertFalse(settings.EnableCustomCommands)
        self.assertEqual(settings.CustomCommandStrings, "!hello;morning;evening")
        self.assertFalse(settings.EnableCustomOutput)
        self.assertEqual(settings.CustomOutputPercentage, 10)
        self.assertIsNot(settings.__dict__, "CustomOutputStrings")
        self.assertFalse(settings.Debug)

    def test_constructor__with_v1_1_0_file__loads_file_with_defaults(self):
        settings_path = os.path.join(os.path.dirname(__file__), "settings_files", "settings-v1.1.0.json")
        custom_output_path = os.path.join(os.path.dirname(__file__), "settings_files", "temp_v1.1.0_outputs.txt")
        settings = ScriptSettings(
            settings_file=settings_path,
            custom_outputs_file=custom_output_path,
        )

        # v1.1.0 available properties
        self.assertEqual(settings.Permission, "user_specific")
        self.assertEqual(settings.Info, "hk_47")
        self.assertEqual(settings.Cooldown, 600)
        self.assertTrue(settings.EnableCustomCommands)
        self.assertEqual(settings.CustomCommandStrings, "!hello;")
        self.assertTrue(settings.Debug)

        # Expected to be default values
        self.assertFalse(settings.EnableCustomOutput)
        self.assertEqual(settings.CustomOutputPercentage, 10)
        self.assertIsNot(settings.__dict__, "CustomOutputStrings")

    def test_constructor__with_v1_2_0_file__loads_file_and_writes_to_custom_outputs(self):
        settings_path = os.path.join(os.path.dirname(__file__), "settings_files", "settings-v1.2.0.json")
        custom_output_path = os.path.join(os.path.dirname(__file__), "settings_files", "temp_v1.2.0_outputs.txt")
        settings = ScriptSettings(
            settings_file=settings_path,
            custom_outputs_file=custom_output_path,
        )

        # v1.2.0 available properties
        self.assertEqual(settings.Permission, "user_specific")
        self.assertEqual(settings.Info, "Pineapple")
        self.assertEqual(settings.Cooldown, 10)
        self.assertTrue(settings.EnableCustomCommands)
        self.assertEqual(settings.CustomCommandStrings, "!hello;!boo")
        self.assertTrue(settings.Debug)
        self.assertTrue(settings.EnableCustomOutput)
        self.assertEqual(settings.CustomOutputPercentage, 15)
        self.assertIsNot(settings.__dict__, "CustomOutputStrings")

        # Verify the custom outputs get written to the text file
        custom_output_settings = CustomOutputSettings(
            file_path=custom_output_path,
        )

        result = custom_output_settings.read()
        expected_result = [
            "Well hello Mr. Fancy Pants!",
            "Hello, is it me you are looking for?",
        ]
        self.assertListEqual(result, expected_result)

    def test_initialize__loads_file(self):
        settings = ScriptSettings()
        # This is already verified to load the default values

        json_path = os.path.join(os.path.dirname(__file__), "settings_files", "settings-test.json")
        settings.initialize(json_path)

        # The settings will have the values from the JSON file.
        self.assertEqual(settings.Permission, "everyone")
        self.assertEqual(settings.Info, "Banana")
        self.assertEqual(settings.Cooldown, 10)
        self.assertTrue(settings.EnableCustomCommands)
        self.assertEqual(settings.CustomCommandStrings, "!hello;morning;evening;banana")
        self.assertFalse(settings.EnableCustomOutput)
        self.assertEqual(settings.CustomOutputPercentage, 15)
        self.assertIsNot(settings.__dict__, "CustomOutputStrings")
        self.assertTrue(settings.Debug)

    def test_save__saves_file(self):
        settings = ScriptSettings()
        mock_parent = Mock()

        json_path = os.path.join(os.path.dirname(__file__), "settings_files", "settings-saved.json")
        settings.save(json_path, mock_parent, "Ash")
        mock_parent.assert_not_called()

        # Saving creates the JSON and javascript files.
        js_path = os.path.join(os.path.dirname(__file__), "settings_files", "settings-saved.js")
        self.assertTrue(os.path.isfile(json_path))
        self.assertTrue(os.path.isfile(js_path))

    def test_to_string__outputs_strings(self):
        settings = ScriptSettings()
        self.assertEqual(settings.to_string(),
                         "{'Info': '', 'EnableCustomCommands': False, 'CustomOutputPercentage': 10, "
                         "'CustomCommandStrings': '!hello;morning;evening', 'Permission': 'everyone', "
                         "'Cooldown': 60, 'Debug': False, 'EnableCustomOutput': False}")
