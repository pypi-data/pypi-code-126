from abc import ABC, abstractmethod
from logging import Logger, LoggerAdapter
from typing import final

import enc_netzwerkverbindung_heureka_code.server.__client_handler as cl_h

from .verwaltung import RSASchluesselpaar, RSAVerwalter


class ServerKontext(ABC):
    """ Kontext fuer die Verwaltung des Servers """
    def __init__(self, client_handler: "type[cl_h.BasisClientHandler]" = None,
                 rsa_schluesselpaar: RSASchluesselpaar = None):
        """
        Kontext fuer die Verwaltung des Servers

        :param client_handler: Klasse fuer die Verwaltung neuer Anfragen
        :param rsa_schluesselpaar: Instanz zur Generierung des RSA-Schluesselpaares
        """
        self.__client: "type[cl_h.BasisClientHandler]" = client_handler if client_handler else \
            cl_h.BasisClientHandler
        self.__rsa_schluesselpaar: RSASchluesselpaar = rsa_schluesselpaar if rsa_schluesselpaar else RSAVerwalter()

    @abstractmethod
    def get_server_logger(self, name) -> ["Logger", "LoggerAdapter"]:
        """ Generiert einen Logger fuer den Server """
        pass

    @abstractmethod
    def get_client_logger(self, ip) -> ["Logger", "LoggerAdapter"]:
        """ Generiert einen fuer jeden Client individuellen Logger """
        pass

    @final
    def get_rsa(self) -> RSASchluesselpaar:
        """ Liefert das RSA-Schluesselpaar """
        return self.__rsa_schluesselpaar

    @property
    def client_handler(self) -> "type[cl_h.BasisClientHandler]":
        """ Die fuer einkommende Anfragen zu verwendende Klasse """
        return self.__client

    @client_handler.setter
    def client_handler(self, client: "type[cl_h.BasisClientHandler]"):
        """ Setzt die fuer einkommende Anfragen zu verwendende Klasse """
        if issubclass(client, cl_h.BasisClientHandler):
            self.__client = client
