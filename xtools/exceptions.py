class AbstractException(Exception):
    pass


class DriverDoesNotSupported(AbstractException):
    pass


class LoggerException(AbstractException):
    pass


class BrowserNameIsNotValid(AbstractException):
    pass


class OptionIsNotValid(AbstractException):
    pass


class IPIsNotValid(AbstractException):
    pass
