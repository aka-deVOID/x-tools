from logging import debug, info, warning, error, critical

from exceptions import LoggerException


class Logging:
    """Log class to ddeserve log methods for using logging in core classes"""

    @staticmethod
    def log(log_level: str, message: str) -> None:
        """
        :raise LoggerException:
        """
        match log_level:
            case "info":
                info(message)
            case "warning":
                warning(message)
            case "error":
                error(message)
            case "debug":
                debug(message)
            case "critical":
                critical(message)
            case _:
                raise LoggerException(f"{log_level} log level is not valid")


class Abstract(Logging):
    """the top level of abstraction for each core class in twitter tools"""
    pass
