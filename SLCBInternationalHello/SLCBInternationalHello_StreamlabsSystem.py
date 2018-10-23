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
    "Buongiorno",  # Italian
    "Hallo",  # German
    "Guten tag",  # German
    "Moin moin",  # German
    "Namaste",  # Hindi
    "Salaam",  # Farsi
    "Merhaba",  # Turkish
    "Szia",  # Hungarian
    "Hej",  # Swedish, Danish
    "Zdravo",  # Croatian
    "Ahoj",  # Czech
    "Kamusta",  # Flipino
    "Hei",  # Finnish, Norwegian
    "God dag",  # Norwegian
    "Halo",  # Indonesian
    "Sveiki",  # Latvian
    "Salut",  # Romanian, etc
    "Ahoj",  # Slovak
    "Sawubona",  # Zulu
    "Hullo",  # Scottish
    "Dia dhuit",  # Gaelic
    "G'day",  # Australian
    "Aloha",  # Hawaiian
    u'xin ch\xe0o',  # Vietnamese
    u'Dzie\u0144 dobry',  # Polish
    u'Ol\xe1',  # Portugese
    u'\u0e2a\u0e27\u0e31\u0e2a\u0e14\u0e35',  # Thai - swasdi
    u'\u3053\u3093\u306b\u3061\u306f',  # Japanese - Kon'nichiwa
    u'\u3082\u3057\u3082\u3057',  # Japanese - Moshi Moshi
    u'\uc5ec\ubcf4\uc138\uc694',  # Korean - yeoboseyo
    u'\u0421\u0430\u0439\u043d \u0443\u0443',  # Mongolian - Sain uu
    u'\u0421\u04d9\u043b\u0435\u043c\u0435\u0442\u0441\u0456\u0437 \u0431\u0435',  # Kazakh - Salemetsiz be
    u'\u041f\u0440\u0438\u0432\u0435\u0442',  # Russian - Privet
    u'\u4f60\u597d',  # Chinese - Ni Hao
    u'P\xebrsh\xebndetje',  # Albanian
    u'\u1230\u120b\u121d',  # Amharic - selami
    u'\u0645\u0631\u062d\u0628\u0627',  # Arabic - marhabaan
    u'\u03b3\u03b5\u03b9\u03b1 \u03c3\u03b1\u03c2',  # Greek - geia sas
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

    initialize_input_greetings()
    log("Recognized input greetings:{}".format(InputGreetings))
    return


def initialize_input_greetings():
    InputGreetings = []
    for greeting in Greetings:
        InputGreetings.append(greeting.lower())

    if not ScriptSettings.EnableCustomCommands:
        return

    custom_commands_string = ScriptSettings.CustomCommandStrings
    log("Custom commands string:{}".format(custom_commands_string))

    custom_commands = parse_custom_commands(custom_commands_string)
    log("Parsed custom commands listed:{}".format(custom_commands))

    for custom_command in custom_commands:
        InputGreetings.append(custom_command)
    return


def parse_custom_commands(commands_string):
    custom_commmands = []
    commands_array = commands_string.split(";")
    for command_string in commands_array:
        cleaned_command_string = command_string.strip()
        if cleaned_command_string:
            # The input is valid and is not empty.
            custom_commmands.append(cleaned_command_string)
    return custom_commmands


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
    pool_length = len(Greetings)
    random_array = [random.randint(0, pool_length * pool_length) % pool_length for p in range(0, 20)]
    log("Random selection pool: {}".format(random_array))
    random_index = random.choice(random_array)

    is_reverse_index = random.randint(0, 1)
    if is_reverse_index:
        random_index = pool_length - random_index - 1

    greeting = Greetings[random_index]
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
    initialize_input_greetings()
    log("Recognized input greetings:{}".format(InputGreetings))
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
