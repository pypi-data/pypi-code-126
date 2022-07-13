import logging


class LoggingKontext:
    """ Kontext fuer den Start und das Ende verschiedener Prozesse """
    def __init__(self, logger, betreff: str,
                 level_enter=logging.DEBUG, level_exit=logging.INFO,
                 verb_enter: str = " begonnen.",
                 verb_exit: str = " abgeschlossen.",
                 verb_error: str = " konnte nicht abgeschlossen werden"):
        """ Kontext fuer den Start und das Ende verschiedener Prozesse """
        self._logger = logger
        self.betreff = betreff
        self.level_enter = level_enter
        self.level_exit = level_exit
        self.verb_enter: str = verb_enter
        self.verb_exit: str = verb_exit
        self.verb_error: str = verb_error

    def __enter__(self):
        """ Initiale Nachricht zum Anfang des Prozesses """
        self._logger.log(level=self.level_enter, msg=self.betreff + self.verb_enter)
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        """ Ende des Blocks """
        if exc_val:
            self._logger.exception(exc_val)
            self._logger.exception(self.betreff + self.verb_error)
        else:
            self._logger.log(level=self.level_exit, msg=self.betreff + self.verb_exit)
        pass
    pass
