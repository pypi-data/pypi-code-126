class User(dict):
    """ Klasse zur Weiterleitung von Benutzerdaten """
    def __init__(self, dic):
        """ Klasse zur Weiterleitung von Benutzerdaten """
        super(User, self).__init__(dic)

    @property
    def vorname(self) -> str:
        """ Der Vorname des Benutzers """
        return self["Vorname"]

    @property
    def nachname(self) -> str:
        """ Der Nachname des Benutzers """
        return self["Nachname"]

    @property
    def passwort(self) -> str:
        """ Das Passwort des Benutzers """
        return self["Passwort"]

    def __repr__(self):
        """ Stellt einen Benutzer dar """
        return f"<Benutzer {self.vorname} {self.nachname} ({self.passwort})>"
