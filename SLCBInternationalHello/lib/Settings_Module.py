import codecs
import json


class CommandSettings(object):
    # Yeah... I know the values are different type.
    # But it is better to have the defaults in one place than spread out all over in multiple functions.
    DEFAULT_VALUES_DICTIONARY = {
        "Permission": "everyone",
        "Info": "",
        "Cooldown": 60,
        "EnableCustomCommands": False,
        "CustomCommandStrings": "!hello;morning;evening",
        "EnableCustomOutput": False,
        "CustomOutputPercentage": 10,
        "CustomOutputStrings": (
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
            ),
        "Debug": False,
    }

    def __init__(self, settingsfile=None):
        try:
            with codecs.open(settingsfile, encoding="utf-8-sig", mode="r") as f:
                self.__dict__ = json.load(f, encoding="utf-8")
        except:
            # Expect the open to fail if the file does not exist
            pass

        self.initialize_defaults()

    def Reload(self, jsondata):
        self.__dict__ = json.loads(jsondata, encoding="utf-8")
        return

    def Save(self, settingsfile, parent=None, script_name=None):
        try:
            with codecs.open(settingsfile, encoding="utf-8-sig", mode="w+") as f:
                json.dump(self.__dict__, f, encoding="utf-8")
            with codecs.open(settingsfile.replace("json", "js"), encoding="utf-8-sig", mode="w+") as f:
                f.write("var settings = {0};".format(json.dumps(self.__dict__, encoding='utf-8')))
        except Exception as e:
            if parent:
                parent.Log(script_name, "Failed to save settings to file: {}".format(e))
        return

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
