from .ablauf_verwalter import Verbindungsablauf
from enc_netzwerkverbindung_heureka_code.server.__dict_benutzer import User
from enc_netzwerkverbindung_heureka_code.__generell import LoggingKontext
import logging
import json


class AblaufBenutzer(Verbindungsablauf):
    def receive_user(self) -> User:
        with LoggingKontext(self.logger, "Userdaten empfangen", level_enter=logging.DEBUG, level_exit=logging.DEBUG):
            user = self.handler.verbindung.receive_encrypted()

        with LoggingKontext(self.logger, "Userdaten ", verb_enter="werden geparst", verb_exit=" wurden geparst",
                            level_exit=logging.DEBUG):
            user_json = User(json.loads(user.decode("utf-8")))
        return user_json

    def user_akzeptieren(self, user: User):
        if self.handler.server_kontext.user_akzeptieren(user):
            self.logger.info(f"{user} wurde akzeptiert")
            self.handler.verbindung.send_encrypted("ACCEPTED".encode("utf-8"))
            return True
        else:
            self.logger.info(f"User {user_json} wurde abgelehnt")
            self.handler.verbindung.send_encrypted("REJECTED".encode("utf-8"))
        return False

    pass
