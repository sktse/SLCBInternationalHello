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
Version = "1.0.0.0"

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
    "Allo",
    "Bonjour",
    "Top-o-the-morning",
    "Hola",
    "Ciao",
    "Hallo",
    "Guten tag",
    "Namaste",
    "Salaam",
    "Merhaba",
    "Szia",
    "Hej",
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
        return

    if not Parent.HasPermission(data.User, ScriptSettings.Permission, ScriptSettings.Info):
        # The user does not have permission to trigger this command
        return

    if Parent.IsOnUserCooldown(ScriptName, CommandConstant, data.User)
        # The user is on cooldown for this command
        return

    if first_param in InputGreetings:
        greeting_message = PickGreeting(data.User)
        Parent.SendStreamMessage(greeting_message)
        Parent.AddUserCooldown(ScriptName, CommandConstant, data.User, ScriptSettings.Cooldown)


    # if data.IsChatMessage() and Parent.IsOnUserCooldown(ScriptName, ScriptSettings.Command, data.User):
    #     remaining_timeout = Parent.GetUserCooldownDuration(ScriptName, ScriptSettings.Command, data.User)
    #     Parent.SendStreamMessage("Time Remaining for {}:{}".format(data.user, remaining_timeout)
    #   Check if the propper command is used, the command is not on cooldown and the user has permission to use the command
    # if data.IsChatMessage() and not Parent.IsOnUserCooldown(ScriptName,ScriptSettings.Command,data.User) and Parent.HasPermission(data.User,ScriptSettings.Permission,ScriptSettings.Info):
    #     Parent.BroadcastWsEvent("EVENT_MINE","{'show':false}")
    #     Parent.SendStreamMessage(ScriptSettings.Response)    # Send your message to chat
    #     Parent.AddUserCooldown(ScriptName,ScriptSettings.Command,data.User,ScriptSettings.Cooldown)  # Put the command on cooldown
    #

    return

def PickGreeting(user):
    greeting = random.choice(Greetings)
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

    if "$myparameter" in parseString:
        return parseString.replace("$myparameter","I am a cat!")

    return parseString

#---------------------------
#   [Optional] Reload Settings (Called when a user clicks the Save Settings button in the Chatbot UI)
#---------------------------
def ReloadSettings(jsonData):
    # Execute json reloading here
    ScriptSettings.__dict__ = json.loads(jsonData)
    ScriptSettings.Save(SettingsFile)
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
