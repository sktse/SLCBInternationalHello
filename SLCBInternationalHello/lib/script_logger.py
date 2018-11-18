class StreamlabsChatbotScriptLogger(object):
    def __init__(self, log_name=None, parent=None, is_enabled=False):
        self.log_name = log_name
        self.parent = parent
        self.is_enabled = is_enabled

    def log(self, message):
        if self.is_enabled:
            self.parent.Log(self.log_name, message)

    def set_enabled(self, is_enabled):
        self.is_enabled = is_enabled
