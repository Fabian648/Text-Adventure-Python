
class TA_Error(Exception):

    def __init__(self, message=None):
        
        self.message = message
        super().__init__(message)


class NotImplementedError(TA_Error):
    pass

class ModuleNotFoundError(TA_Error):
    pass

class NotARaceError(TA_Error):
    pass

class InvalidStats(TA_Error):
    pass