import codecs
import json
import os

from constants import ScriptConstants
from parsers import (
    NewLineSeparatedFileParser,
    SemicolonSeparatedParser,
)


class ScriptSettings(object):
    DEFAULT_VALUES_DICTIONARY = {
        "Permission": "everyone",
        "Info": "",
        "Cooldown": 60,
        "EnableCustomCommands": False,
        "CustomCommandStrings": "!hello;morning;evening",
        "EnableCustomOutput": False,
        "CustomOutputPercentage": 10,
        "Debug": False,
    }

    # These are the keys we are writing to the settings JSON.
    # This is a subset of keys because we have stopped using some keys.
    SETTINGS_WRITE_KEYS = [
        "Permission",
        "Info",
        "Cooldown",
        "EnableCustomCommands",
        "CustomCommandStrings",
        "EnableCustomOutput",
        "CustomOutputPercentage",
        "Debug",
    ]

    def __init__(self, settings_file=None, custom_outputs_file=None):
        if settings_file:
            self.initialize(settings_file)

        default_custom_outputs_path = os.path.join(os.path.join(os.path.dirname(__file__), "..", "custom_outputs.txt"))
        self.custom_outputs_file = custom_outputs_file or default_custom_outputs_path

        self.initialize_defaults()
        self.upgrade()

        # Initialize the custom out text file manager.
        self.custom_output_settings = CustomOutputSettings(
            file_path=self.custom_outputs_file,
        )

    def initialize(self, settings_file):
        try:
            with codecs.open(settings_file, encoding="utf-8-sig", mode="r") as f:
                self.__dict__ = json.load(f, encoding="utf-8")
        except:
            # Expect the open to fail if the file does not exist
            pass

    def upgrade(self):
        config_version = self.__dict__.get("VERSION", "1.2.0")
        if config_version == "1.2.0":
            config_version = "1.3.0"
            # Unfortunately v1.1.0 does not have "CustomOutputStrings"
            if "CustomOutputStrings" in self.__dict__:
                # Dropped "CustomOutputStrings" because it is written to a file now.
                custom_output_strings_list = SemicolonSeparatedParser.parse(self.CustomOutputStrings)
                custom_output_settings = CustomOutputSettings(
                    file_path=self.custom_outputs_file,
                )
                custom_output_settings.write(custom_output_strings_list)
                del self.CustomOutputStrings

        # Save the changes to the settings file
        self.save(script_name=ScriptConstants.SCRIPT_NAME)

    def reload(self, jsondata):
        self.__dict__ = json.loads(jsondata, encoding="utf-8")
        return

    def build_save_dictionary(self):
        save_dictionary = {}
        for key in self.SETTINGS_WRITE_KEYS:
            save_dictionary[key] = self.__dict__[key]

        save_dictionary["VERSION"] = ScriptConstants.VERSION
        return save_dictionary

    def save(self, settingsfile=None, parent=None, script_name=None):
        default_file_path = os.path.join(os.path.join(os.path.dirname(__file__), "..", "Settings", "settings.json"))
        settings_path = settingsfile or default_file_path

        save_dictionary = self.build_save_dictionary()
        try:
            with codecs.open(settings_path, encoding="utf-8-sig", mode="w+") as f:
                json.dump(save_dictionary, f, encoding="utf-8")
            with codecs.open(settings_path.replace("json", "js"), encoding="utf-8-sig", mode="w+") as f:
                f.write("var settings = {0};".format(json.dumps(save_dictionary, encoding='utf-8')))
        except Exception as e:
            if parent:
                parent.Log(script_name, "Failed to save settings to file: {}".format(e))
        return

    def get_custom_output_strings(self):
        return self.custom_output_settings.read()

    def to_string(self):
        self_dict = {}
        for key in self.DEFAULT_VALUES_DICTIONARY.keys():
            self_dict[key] = getattr(self, key)

        return str(self_dict)

    def initialize_defaults(self):
        """
        Goes through all settings properties to check if they exist.
        If the property does not exist, set it to the default value for that property.

        The loaded JSON settings file may not have all the properties.
        This is the upgrade scenario where the newer version has new properties that the JSON file does not.
        """
        for key in self.DEFAULT_VALUES_DICTIONARY.keys():
            if not hasattr(self, key):
                value = self.DEFAULT_VALUES_DICTIONARY.get(key)
                setattr(self, key, value)


class CustomOutputSettings:
    def __init__(self, file_path=None):
        default_file_path = os.path.join(os.path.join(os.path.dirname(__file__), "..", "custom_outputs.txt"))
        self.file_path = file_path or default_file_path
        self.parser = NewLineSeparatedFileParser(file_path=self.file_path)

    def read(self):
        return self.parser.read()

    def write(self, lines):
        self.parser.write(lines)
