class InputError(Exception):
    def __init__(self, exceptions, message):
        self.exception = exceptions
        self.message = message