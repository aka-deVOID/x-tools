class AbstractException(Exception):
    pass


class DriverDoesNotSupported(AbstractException):
    pass


class LoggerException(AbstractException):
    pass


class BrowserNameIsNotValid(AbstractException):
    pass
