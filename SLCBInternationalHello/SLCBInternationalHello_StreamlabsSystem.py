#---------------------------
#   Import Libraries
#---------------------------
import json
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "lib"))  # point at lib folder for classes / references

import clr
clr.AddReference("IronPython.SQLite.dll")
clr.AddReference("IronPython.Modules.dll")

from better_random import BetterRandom
from constants import ScriptConstants
from script_logger import StreamlabsChatbotScriptLogger
from settings import ScriptSettings


#---------------------------
#   [Required] Script Information
#---------------------------
ScriptName = ScriptConstants.SCRIPT_NAME
Website = ScriptConstants.WEBSITE
Description = ScriptConstants.DESCRIPTION
Creator = ScriptConstants.CREATOR
Version = ScriptConstants.VERSION

#---------------------------
#   Define Global Variables
#---------------------------
global script_settings
script_settings = ScriptSettings()
global logger
logger = StreamlabsChatbotScriptLogger()
global Greetings
Greetings = []
global InputGreetings
InputGreetings = []
global CustomOutputGreetings
CustomOutputGreetings = []


#---------------------------
#   [Required] Initialize Data (Only called on load)
#---------------------------
def Init():

    #   Create Settings Directory
    directory = os.path.join(os.path.dirname(__file__), "Settings")
    if not os.path.exists(directory):
        os.makedirs(directory)

    #   Load settings
    settings_file = os.path.join(os.path.dirname(__file__), "Settings\settings.json")
    script_settings = ScriptSettings(settings_file)

    initialize_script()
    return


def get_parent():
    """
    Wrapper function for the Parent object.
    It is magically injected by Streamlabs Chatbot
    :return: The Parent object
    """
    return Parent


def initialize_script():
    logger = StreamlabsChatbotScriptLogger(ScriptConstants.SCRIPT_NAME, get_parent(), script_settings.Debug)

    initialize_input_greetings()
    logger.log("Recognized input greetings:{}".format(InputGreetings))

    initialize_custom_output_greetings()
    logger.log("Recognized custom output greetings:{}".format(CustomOutputGreetings))


def initialize_input_greetings():
    del Greetings[:]
    Greetings.extend(ScriptConstants.DEFAULT_GREETINGS)

    # Delete the contents of the array but NOT creating a new instance
    # The pointer needs to be the same, but the contents nuked.
    del InputGreetings[:]
    for greeting in Greetings:
        InputGreetings.append(greeting.lower())

    logger.log("Standard set of input greetings:{}".format(InputGreetings))

    logger.log("Is custom input commands enabled? {}".format(script_settings.EnableCustomCommands))
    if not script_settings.EnableCustomCommands:
        return

    custom_commands_string = script_settings.CustomCommandStrings
    logger.log("Custom commands string:{}".format(custom_commands_string))

    custom_commands = parse_custom_commands(custom_commands_string)
    logger.log("Parsed custom commands listed:{}".format(custom_commands))

    for custom_command in custom_commands:
        InputGreetings.append(custom_command)

    logger.log("Extended set of input greetings:{}".format(InputGreetings))
    return


def initialize_custom_output_greetings():
    # Delete the contents of the array but NOT creating a new instance
    # The pointer needs to be the same, but the contents nuked.
    del CustomOutputGreetings[:]

    logger.log("Is custom output commands enabled? {}".format(script_settings.EnableCustomOutput))
    if not script_settings.EnableCustomOutput:
        return

    custom_outputs_string = script_settings.CustomOutputStrings
    logger.log("Custom outputs string:{}".format(custom_outputs_string))

    custom_outputs = parse_custom_commands(custom_outputs_string)
    logger.log("Parsed custom outputs listed:{}".format(custom_outputs))

    for custom_output in custom_outputs:
        CustomOutputGreetings.append(custom_output)

    logger.log("Custom set of output greetings:{}".format(CustomOutputGreetings))
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
    parent = get_parent()

    if not data.IsChatMessage():
        # Only interested in picking up chat messages
        return

    # This is the first word that the User typed
    first_param = data.GetParam(0).lower().strip()

    if first_param not in InputGreetings:
        # The user did not say a greeting
        logger.log("User [{}] did not say hello".format(data.User))
        return

    if not parent.HasPermission(data.User, script_settings.Permission, script_settings.Info):
        # The user does not have permission to trigger this command
        logger.log("User [{}] does not have permission".format(data.User))
        return

    if parent.IsOnUserCooldown(ScriptName, ScriptConstants.SCRIPT_KEY, data.User):
        # The user is on cool down for this command
        cooldown_remaining = parent.GetUserCooldownDuration(ScriptName, ScriptConstants.SCRIPT_KEY, data.User)
        logger.log("User [{}] is still on cooldown for: {}".format(data.User, cooldown_remaining))
        return

    if first_param in InputGreetings:
        greeting_message = pick_random_greeting(data.User)
        logger.log("User [{}] triggered the reply: {}".format(data.User, greeting_message))
        parent.SendStreamMessage(greeting_message)

        cooldown_in_seconds = int(script_settings.Cooldown) * 60
        parent.AddUserCooldown(ScriptName, ScriptConstants.SCRIPT_KEY, data.User, cooldown_in_seconds)

    return


def pick_random_greeting(user):
    greeting_set = Greetings if pick_greeting_type() else CustomOutputGreetings
    greeting = pick_greeting(greeting_set)
    return format_greeting(greeting, user)


def pick_greeting_type():
    """
    CustomOutputPercentage is between 1 and 100
    if the roll is less than CustomOutputPercentage, then it is custom greeting.  Otherwise default greeting.
    Example:
        * CustomOutputPercentage == 1 percent, roll is 0 ==> Show custom greeting.
        * CustomOutputPercentage == 1 percent, roll is 1+ ==> Show default greeting.

    This means, show custom greeting is
    ```
    is_custom_greeting = randomIndex < CustomOutputPercentage
    ```

    Therefore, show the default greeting is
    ```
    is_default_greeting = not is_custom_greeting
    is_default_greeting = not randomIndex < CustomOutputPercentage
    is_default_greeting = randomIndex >= CustomOutputPercentage
    ```

    :return: True if the default greeting. False for custom greeting.
    """

    if not script_settings.EnableCustomOutput:
        # if custom output greetings is disabled, just exit out immediately with default greetings.
        return True

    if script_settings.CustomOutputPercentage == 0:
        # if custom output greetings is set to 0%, just exit out immediately with default greetings.
        return True

    random_index = BetterRandom.random(100)
    is_default_greeting = random_index >= script_settings.CustomOutputPercentage
    logger.log("Is greeting type default? {}".format(is_default_greeting))

    return is_default_greeting


def pick_greeting(greeting_set):
    """
    Randomly picks a greeting from the given set of greetings
    :param greeting_set: The array of greetings
    :return: A single greeting string
    """
    random_index = BetterRandom.random(len(greeting_set))
    greeting = greeting_set[random_index]
    return greeting


def format_greeting(greeting, user):
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
    settings_file = os.path.join(os.path.dirname(__file__), "Settings", "settings.json")
    script_settings.__dict__ = json.loads(jsonData)
    script_settings.save(settings_file, get_parent(), ScriptName)
    logger.log("Active script settings: {}".format(script_settings.to_string()))

    initialize_script()
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
