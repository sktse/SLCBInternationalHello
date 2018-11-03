import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../SLCBInternationalHello/lib"))  # Manually import

from unittest import TestCase

from Settings_Module import CommandSettings


class SettingsModuleTests(TestCase):
    def test_default_constructor__setups_default_values(self):
        settings = CommandSettings()
        self.assertEqual(settings.Permission, "everyone")
        self.assertEqual(settings.Info, "")
        self.assertEqual(settings.Cooldown, 60)
        self.assertFalse(settings.EnableCustomCommands)
        self.assertEqual(settings.CustomCommandStrings, "")
        self.assertFalse(settings.Debug)
