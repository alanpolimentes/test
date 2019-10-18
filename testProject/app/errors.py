class InvalidInput(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

    def __str__(self):
        return self.message