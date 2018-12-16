import logging

logger = logging.getLogger()


class StreamlabsChatbotScriptLogger(object):
    def __init__(self, log_name=None, parent=None, is_enabled=False, is_debug=False):
        self.log_name = log_name
        self.parent = parent
        self.is_enabled = is_enabled
        self.is_debug = is_debug

    def log(self, message):
        if self.is_debug:
            logger.info(message)

        if self.is_enabled:
            self.parent.Log(self.log_name, message)

    def set_enabled(self, is_enabled):
        self.is_enabled = is_enabled
