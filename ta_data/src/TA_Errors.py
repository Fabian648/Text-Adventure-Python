import sys
sys.path.append(".")
from ta_data.src.modules import Logger


class TA_Error(Exception):
    def __init__(self, message=None, error=Exception):
        Logger().error_log(logtext=message, error=error)

class NotImplementedError(TA_Error):
    def __init__(self, message=None):
        super().__init__(message=message, error=NotImplementedError)

class ModuleNotFoundError(TA_Error):
    def __init__(self, message=None):
        super().__init__(message=message, error=ModuleNotFoundError)

class NotARaceError(TA_Error):
    def __init__(self, message=None):
        super().__init__(message=message, error=NotARaceError)

class InvalidStats(TA_Error):
    def __init__(self, message=None):
        super().__init__(message=message, error=InvalidStats)
        
class InventoryIntegretyError(TA_Error):
    def __init__(self, message=None):
        super().__init__(message=message, error=InventoryIntegretyError)

class FileLoadError(TA_Error):
    def __init__(self, message=None):
        super().__init__(message=message, error=FileLoadError)

class CriticalFightError(TA_Error):
    def __init__(self, message=None):
        super().__init__(message=message, error=CriticalFightError)

class NoSavedGame(TA_Error):
    def __init(self, message=None):
        super().__init__(message=message, error=NoSavedGame)

