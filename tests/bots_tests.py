import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../SLCBInternationalHello/lib"))  # Manually import

from unittest import TestCase
from mock import (
    MagicMock,
    patch,
)

from bots import HelloBot
from constants import ScriptConstants
from detectors import GreetingDetector
from settings import ScriptSettings


class HelloBotTests(TestCase):
    def setUp(self):
        self.mock_parent = MagicMock()
        self.script_settings = ScriptSettings()

        self.greetings = []
        for greeting in ScriptConstants.DEFAULT_GREETINGS:
            lower_greeting = greeting.lower()
            self.greetings.append(lower_greeting)

        self.detector = GreetingDetector()
        self.detector.initialize(self.greetings)

        self.custom_output_greetings = []
        self.logger = MagicMock()

        self.bot = HelloBot()
        self.bot.initialize(
            parent=self.mock_parent,
            script_settings=self.script_settings,
            greeting_detector=self.detector,
            greetings=self.greetings,
            custom_output_greetings=self.custom_output_greetings,
            logger=self.logger,
        )

        self.mock_data = MagicMock()
        self.mock_data.User = "rogukalth"

    def test_execute__with_data_is_not_message__exits_early(self):
        self.mock_data.IsChatMessage.return_value = False
        with patch.object(GreetingDetector, 'is_greeting', wraps=self.detector.is_greeting) as mock_is_greeting:
            self.bot.execute(self.mock_data)
            mock_is_greeting.assert_not_called()

    def test_execute__with_not_a_greeting__exits_early(self):
        self.mock_data.IsChatMessage.return_value = True
        self.mock_data.GetParamCount.return_value = 1
        self.mock_data.GetParam.return_value = "goodbye"

        self.bot.execute(self.mock_data)

        self.logger.log.assert_called_once_with("User [rogukalth] did not say hello")
        self.mock_parent.HasPermission.assert_not_called()

    def test_execute__with_no_permission__exits_early(self):
        self.mock_data.IsChatMessage.return_value = True
        self.mock_data.GetParamCount.return_value = 1
        self.mock_data.GetParam.return_value = "aloha"
        self.mock_parent.HasPermission.return_value = False

        self.bot.execute(self.mock_data)

        self.logger.log.assert_called_once_with("User [rogukalth] does not have permission")
        self.mock_parent.HasPermission.assert_called_once_with("rogukalth", "everyone", "")

    def test_execute__with_user_on_cooldown__exits_early(self):
        self.mock_data.IsChatMessage.return_value = True
        self.mock_data.GetParamCount.return_value = 1
        self.mock_data.GetParam.return_value = "aloha"
        self.mock_parent.HasPermission.return_value = True
        self.mock_parent.IsOnUserCooldown.return_value = True
        self.mock_parent.GetUserCooldownDuration.return_value = 31415

        with patch.object(HelloBot, 'pick_greeting', wraps=self.bot.pick_greeting) as mock_pick_greeting:
            self.bot.execute(self.mock_data)
            mock_pick_greeting.assert_not_called()

        self.logger.log.assert_called_once_with("User [rogukalth] is still on cooldown for: 31415")

    def test_execute__with_greeting__sends_greeting(self):
        self.mock_data.IsChatMessage.return_value = True
        self.mock_data.GetParamCount.return_value = 1
        self.mock_data.GetParam.return_value = "aloha"
        self.mock_parent.HasPermission.return_value = True
        self.mock_parent.IsOnUserCooldown.return_value = False

        self.bot.greeting_picker = MagicMock()
        self.bot.greeting_picker.pick.return_value = "Moin moin"

        self.bot.execute(self.mock_data)

        self.logger.log.assert_called_once_with("User [rogukalth] triggered the reply: Moin moin @rogukalth")
        self.mock_parent.SendStreamMessage.assert_called_once_with("Moin moin @rogukalth")
        self.mock_parent.AddUserCooldown.assert_called_once_with(
            "International Hello",
            "sktse-HelloReply",
            "rogukalth",
            3600,
        )
