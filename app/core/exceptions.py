class LLMError(Exception):
    """Exception raised for errors in LLM operations."""
    pass

class ConfigurationError(Exception):
    """Exception raised for configuration errors."""
    def __init__(self, message, config_key=None):
        super().__init__(message)
        self.config_key = config_key
