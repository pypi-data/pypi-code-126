from .ablauf_verwalter import Verbindungsablauf
import time
from enc_netzwerkverbindung_heureka_code.server.__test import Test


class AblaufTest(Verbindungsablauf):
    def get_erwarteten_test(self) -> Test:
        test = None
        while test is None:
            test = self.handler.server_kontext.get_test()
            time.sleep(0.2)
        self.logger.info(f"{test} wurde geladen")
        return Test.from_obj(test)

    def __init__(self, handler, ist_test_aktiv_func):
        self.__start_zeit: datetime.datetime = datetime.datetime.now()
        self.__ist_test_aktiv = ist_test_aktiv_func
        super(AblaufTest, self).__init__(handler)
        pass

    def test_starten(self):
        self.__start_zeit = datetime.datetime.now()

    def test_beenden(self, test):
        self.__erlaubtes_delta = datetime.timedelta(minutes=test.dauer, seconds=39)
        self.__erlaubtes_ende = self.__start_zeit + self.__erlaubtes_delta
        self.__wirklich_genutzte_zeit = datetime.datetime.now()

    @property
    def abgabe_zulaessig(self) -> bool:
        return self.__wirklich_genutzte_zeit <= self.__erlaubtes_ende and self.__ist_test_aktiv()

    @property
    def vorzeitig_beendet(self) -> bool:
        return not self.__ist_test_aktiv()
