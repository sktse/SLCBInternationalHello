import codecs
import json


class CommandSettings(object):
    def __init__(self, settingsfile=None):
        try:
            with codecs.open(settingsfile, encoding="utf-8-sig", mode="r") as f:
                self.__dict__ = json.load(f, encoding="utf-8")
        except:
            self.Permission = "everyone"
            self.Info = ""
            self.Cooldown = 60
            self.EnableCustomCommands = False
            self.CustomCommandStrings = "!hello;morning;evening"
            self.EnableCustomOutput = False
            self.CustomOutputPercentage = 10
            self.CustomOutputStrings = ("Well hello Mr. Fancy Pants!;"  # Army of Darkness (1992)
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
            self.Debug = False

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
                parent.Log(script_name, "Failed to save settings to file.: {}".format(e))
        return

    def to_string(self):
        self_dict = {
            "Permission": self.Permission,
            "Info": self.Info,
            "Cooldown": self.Cooldown,
            "EnableCustomCommands": self.EnableCustomCommands,
            "CustomCommandStrings": self.CustomCommandStrings,
            "EnableCustomOutput": self.EnableCustomOutput,
            "CustomOutputPercentage": self.CustomOutputPercentage,
            "CustomOutputStrings": self.CustomOutputStrings,
            "Debug": self.Debug
        }
        return str(self_dict)
