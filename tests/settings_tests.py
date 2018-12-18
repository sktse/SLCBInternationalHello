import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../SLCBInternationalHello/lib"))  # Manually import

from unittest import TestCase
from mock import Mock

from settings import ScriptSettings


class ScriptSettingsTests(TestCase):
    def setUp(self):
        self.expected_custom_commands_strings = (
            "Well hello Mr. Fancy Pants!;"  # Army of Darkness (1992)
            "Say 'hello' to my little friend!;"  # Scarface (1983)
            "Hello, my name is Inigo Montoya. You killed my father. Prepare to die.;"  # The Princess Bride 1987
            "Heeeeere's Johnny!;"  # The Shining (1980)
            "You had me at 'Hello'.;"  # Jerry Maguire (1996)
            "You talkin' to me?;"  # Taxi Driver (1976)
            "Live long and prosper.;"  # OG Star Trek
            "Here's looking at you, kid.;"  # Casablanca (1942)
            "Frankly, my dear, I don't give a damn.;"  # Gone With the Wind (1939)
            "Shane. Shane. Come back!;"  # Shane (1953)
            "Mrs. Robinson, you're trying to seduce me. Aren't you?;"  # The Graduate (1967)
            "Yo, Adrian!;"  # Rocky (1976)
            "May the Force be with you.;"  # Star Wars (1977)
            "That'll do, pig, that'll do.;"  # Babe (1995)
            "Hello, is it me you are looking for?;"  # Hello - Lionel Richie (1984)
        )

    def test_default_constructor__setups_default_values(self):
        settings = ScriptSettings()
        self.assertEqual(settings.Permission, "everyone")
        self.assertEqual(settings.Info, "")
        self.assertEqual(settings.Cooldown, 60)
        self.assertFalse(settings.EnableCustomCommands)
        self.assertEqual(settings.CustomCommandStrings, "!hello;morning;evening")
        self.assertFalse(settings.EnableCustomOutput)
        self.assertEqual(settings.CustomOutputPercentage, 10)
        self.assertEqual(settings.CustomOutputStrings, self.expected_custom_commands_strings)
        self.assertFalse(settings.Debug)

    def test_constructor__with_v1_1_0_file__loads_file_with_defaults(self):
        path = os.path.join(os.path.dirname(__file__), "settings_files", "settings-v1.1.0.json")
        settings = ScriptSettings(path)

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
        self.assertEqual(settings.CustomOutputStrings, self.expected_custom_commands_strings)

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
        self.assertEqual(settings.CustomOutputStrings, self.expected_custom_commands_strings)
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
                         "'CustomOutputStrings': \"Well hello Mr. Fancy Pants!;Say 'hello' to my little friend!;"
                         "Hello, my name is Inigo Montoya. You killed my father. Prepare to die.;Heeeeere\'s Johnny!;"
                         "You had me at 'Hello'.;You talkin' to me?;Live long and prosper.;Here's looking at you, kid.;"
                         "Frankly, my dear, I don't give a damn.;Shane. Shane. Come back!;Mrs. Robinson, you're trying "
                         "to seduce me. Aren't you?;Yo, Adrian!;May the Force be with you.;That'll do, pig, that'll do."
                         ";Hello, is it me you are looking for?;\", 'Cooldown': 60, 'Debug': False, "
                         "'EnableCustomOutput': False}")
