import sys
sys.path.append(".")
from ta_data.src.modules import Logger


class TA_Error(Exception):
    pass

class NotImplementedError(TA_Error):
    def __init__(self, message=None):
        Logger().error_log(logtext=message, error=NotImplementedError)

class ModuleNotFoundError(TA_Error):
    def __init__(self, message=None):
        Logger().error_log(logtext=message, error=ModuleNotFoundError)

class NotARaceError(TA_Error):
    def __init__(self, message=None):
        Logger().error_log(logtext=message, error=NotARaceError)

class InvalidStats(TA_Error):
    def __init__(self, message=None):
        Logger().error_log(logtext=message, error=InvalidStats)
        
        

