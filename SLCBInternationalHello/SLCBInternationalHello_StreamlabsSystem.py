#---------------------------
#   Import Libraries
#---------------------------
import json
import os
import random
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "lib")) #point at lib folder for classes / references

import clr
clr.AddReference("IronPython.SQLite.dll")
clr.AddReference("IronPython.Modules.dll")

#   Import your Settings class
from Settings_Module import CommandSettings
#---------------------------
#   [Required] Script Information
#---------------------------
ScriptName = "International Hello"
Website = "https://github.com/sktse"
Description = "Hello! Is it me you are looking for?"
Creator = "sktse"
Version = "1.0.1"

#---------------------------
#   Define Global Variables
#---------------------------
global CommandConstant
CommandConstant = "HelloReply"
global SettingsFile
SettingsFile = ""
global ScriptSettings
ScriptSettings = CommandSettings()
global Greetings
Greetings = [
    "Hello",
    "Greetings",
    "Hi",
    "Allo",  # French
    "Bonjour",  # French
    "Top-o-the-morning",
    "Hola",  # Spanish
    "Ciao",  # Italian
    "Hallo",  # German
    "Guten tag",  # German
    "Namaste",  # Hindi
    "Salaam",  # Farsi
    "Merhaba",  # Turkish
    "Szia",  # Hungarian
    "Hej",  # Swedish, Danish
    "Zdravo",  # Croatian
    "Ahoj",  # Czech
    "Kamusta",  # Flipino
    "Hei",  # Finnish
    "Halo",  # Indonesian
    "Sveiki",  # Latvian
    "Salut",  # Romanian, etc
    "Ahoj",  # Slovak
    "Sawubona",  # Zulu
    'xin ch\xc3\xa0o',  # Vietnamese
    'Dzie\xc5\x84 dobry',  # Polish
    'Ol\xc3\xa1',  # Portugese
    '\xe3\x81\x93\xe3\x82\x93\xe3\x81\xab\xe3\x81\xa1\xe3\x81\xaf',  # Japanese
    '\xec\x97\xac\xeb\xb3\xb4\xec\x84\xb8\xec\x9a\x94',  # Korean
    '\xd0\xa1\xd0\xb0\xd0\xb9\xd0\xbd \xd1\x83\xd1\x83',  # Mongolian
    '\xd0\xa1\xd3\x99\xd0\xbb\xd0\xb5\xd0\xbc\xd0\xb5\xd1\x82\xd1\x81\xd1\x96\xd0\xb7 \xd0\xb1\xd0\xb5',  # Kazakh
    '\xd0\x9f\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82',  # Russian
    '\xe4\xbd\xa0\xe5\xa5\xbd',  # Chinese
    'P\xc3\xabrsh\xc3\xabndetje',  # Albanian
    '\xe1\x88\xb0\xe1\x88\x8b\xe1\x88\x9d',  # Amharic
    '\xd9\x85\xd8\xb1\xd8\xad\xd8\xa8\xd8\xa7',  # Arabic
    '\xce\xb3\xce\xb5\xce\xb9\xce\xb1 \xcf\x83\xce\xb1\xcf\x82',  # Greek
]
global InputGreetings
InputGreetings = []


#---------------------------
#   [Required] Initialize Data (Only called on load)
#---------------------------
def Init():

    #   Create Settings Directory
    directory = os.path.join(os.path.dirname(__file__), "Settings")
    if not os.path.exists(directory):
        os.makedirs(directory)

    #   Load settings
    SettingsFile = os.path.join(os.path.dirname(__file__), "Settings\settings.json")
    ScriptSettings = CommandSettings(SettingsFile)

    for greeting in Greetings:
        InputGreetings.append(greeting.lower())

    return

#---------------------------
#   [Required] Execute Data / Process messages
#---------------------------
def Execute(data):
    if not data.IsChatMessage():
        # Only interested in picking up chat messages
        return

    # This is the first word that the User typed
    first_param = data.GetParam(0).lower().strip()

    if first_param not in InputGreetings:
        # The user did not say a greeting
        log("User [{}] did not say hello".format(data.User))
        return

    if not Parent.HasPermission(data.User, ScriptSettings.Permission, ScriptSettings.Info):
        # The user does not have permission to trigger this command
        log("User [{}] does not have permission".format(data.User))
        return

    if Parent.IsOnUserCooldown(ScriptName, CommandConstant, data.User):
        # The user is on cool down for this command
        cooldown_remaining = Parent.GetUserCooldownDuration(ScriptName, CommandConstant, data.User)
        log("User [{}] is still on cooldown for: {}".format(data.User, cooldown_remaining))
        return

    if first_param in InputGreetings:
        log("User [{}] is getting a reply!".format(data.User))
        greeting_message = PickGreeting(data.User)
        log("User [{}] triggered the reply: {}".format(data.User, greeting_message))
        Parent.SendStreamMessage(greeting_message)

        cooldown_in_seconds = int(ScriptSettings.Cooldown) * 60
        Parent.AddUserCooldown(ScriptName, CommandConstant, data.User, cooldown_in_seconds)

    return


def log(message):
    if ScriptSettings.Debug:
        Parent.Log(ScriptName, message)
    return

def PickGreeting(user):
    # greeting = random.choice(Greetings)
    # greeting = '\xe4\xbd\xa0\xe5\xa5\xbd'.encode('utf-8')  # Chinese
    greeting = '\u4f60\u597d'
    if user:
        greeting = "{} @{}".format(greeting, user)
    return greeting

#---------------------------
#   [Required] Tick method (Gets called during every iteration even when there is no incoming data)
#---------------------------
def Tick():
    return

#---------------------------
#   [Optional] Parse method (Allows you to create your own custom $parameters)
#---------------------------
def Parse(parseString, userid, username, targetid, targetname, message):
    return parseString

#---------------------------
#   [Optional] Reload Settings (Called when a user clicks the Save Settings button in the Chatbot UI)
#---------------------------
def ReloadSettings(jsonData):
    # Execute json reloading here
    SettingsFile = os.path.join(os.path.dirname(__file__), "Settings\settings.json")
    ScriptSettings.__dict__ = json.loads(jsonData)
    ScriptSettings.Save(SettingsFile, Parent, ScriptName)
    return

#---------------------------
#   [Optional] Unload (Called when a user reloads their scripts or closes the bot / cleanup stuff)
#---------------------------
def Unload():
    return

#---------------------------
#   [Optional] ScriptToggled (Notifies you when a user disables your script or enables it)
#---------------------------
def ScriptToggled(state):
    return
