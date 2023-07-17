from logging import debug, info, warning, error, critical


class Log:
    def log(self, log_level: str, message: str) -> None:
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


class ABC(Log):
    pass
