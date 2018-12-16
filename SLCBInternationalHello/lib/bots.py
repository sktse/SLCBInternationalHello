import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "lib"))  # point at lib folder for classes / references

from better_random import GreetingPicker
from constants import ScriptConstants


class HelloBot:
    def __init__(self,
                 parent,
                 script_settings,
                 greeting_detector,
                 greetings,
                 custom_output_greetings,
                 logger):
        self.parent = None
        self.script_settings = None
        self.greeting_detector = None
        self.greetings = None
        self.custom_output_greetings = None
        self.logger = None
        self.greeting_picker = None
        self.initialize(parent, script_settings, greeting_detector, logger, greetings, custom_output_greetings)

    def initialize(self, parent, script_settings, greeting_detector, logger, greetings, custom_output_greetings):
        self.parent = parent
        self.script_settings = script_settings
        self.greeting_detector = greeting_detector
        self.logger = logger
        self.greetings = greetings
        self.custom_output_greetings = custom_output_greetings
        self.greeting_picker = GreetingPicker(
            self.greetings,
            self.custom_output_greetings,
            script_settings.EnableCustomOutput,
            script_settings.CustomOutputPercentage,
            logger
        )

    def execute(self, data):
        if not data.IsChatMessage():
            # Only interested in picking up chat messages
            return

        # Run the inputs through the greeting detector
        is_greeting = self.greeting_detector.is_greeting(data)

        if not is_greeting:
            # The user did not say a greeting
            self.logger.log("User [{}] did not say hello".format(data.User))
            return

        if not self.parent.HasPermission(data.User, self.script_settings.Permission, self.script_settings.Info):
            # The user does not have permission to trigger this command
            self.logger.log("User [{}] does not have permission".format(data.User))
            return

        if self.parent.IsOnUserCooldown(ScriptConstants.SCRIPT_NAME, ScriptConstants.SCRIPT_KEY, data.User):
            # The user is on cool down for this command
            cooldown_remaining = self.parent.GetUserCooldownDuration(
                ScriptConstants.SCRIPT_NAME,
                ScriptConstants.SCRIPT_KEY,
                data.User)
            self.logger.log("User [{}] is still on cooldown for: {}".format(data.User, cooldown_remaining))
            return

        if is_greeting:
            greeting_message = self.pick_greeting(data.User)
            self.logger.log("User [{}] triggered the reply: {}".format(data.User, greeting_message))
            self.parent.SendStreamMessage(greeting_message)

            cooldown_in_seconds = int(self.script_settings.Cooldown) * 60
            self.parent.AddUserCooldown(
                ScriptConstants.SCRIPT_NAME,
                ScriptConstants.SCRIPT_KEY,
                data.User,
                cooldown_in_seconds)

    def pick_greeting(self, user):
        """
        Picks a random greeting and formats it with the user's name.
        :param user: The calling user
        :return: The greeting string with the user's name
        """
        greeting = self.greeting_picker.pick()
        if user:
            greeting = "{} @{}".format(greeting, user)
        return greeting
