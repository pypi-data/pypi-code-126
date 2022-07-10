import base64
import hashlib
import logging
import socket
import struct
from typing import Generator, Tuple, Union

import pywintypes
import sspi
import sspicon
import win32security
from attrs import define, field
from uhttp import Auth, Request
from uhttp._models import H11Response



def default_logger(logger: Union[logging.Logger, None]) -> logging.Logger:
    return logger or logging.getLogger(__name__)


@define(slots=False)
class NegotiateAuth(Auth):
    service: str = field(default='HTTP')
    username: str = field(default=None)
    domain: str = field(default=None)
    password: str = field(default=None)
    host: str = field(default=None)
    delegate: bool = field(default=False)
    opportunistic_auth: bool = field(default=False)
    logger: logging.Logger = field(default=None, converter=default_logger)
    _auth_info: Tuple[str, str, str] = field(default=None, init=False)

    def __attrs_post_init__(self):
        if self.username is not None:
            self._auth_info = (self.username, self.domain, self.password)

    def auth_flow(self, request: Request) -> Generator[Request, H11Response, None]:
        if request.headers.get("authorization") is not None:
            # If auth header provided do nothing
            yield request
            return
        if not self.opportunistic_auth:
            response: H11Response = yield request
            if response.status_code != 401:
                return
            scheme = None
            allowed_schemes = ("Negotiate", "NTLM")
            proposed_scheme = response.headers.get('www-authenticate')
            if proposed_scheme is None:
                return
            for auth_header in proposed_scheme.split(','):
                if auth_header.strip() in allowed_schemes:
                    scheme = auth_header.strip()
                    break
            if not scheme:
                # Server did not respond with Negotiate or NTLM
                return
            if response.headers.get("set-cookie") is not None:
                request.headers["cookie"] = response.headers["set-cookie"]
        else:
            scheme = 'Negotiate'
        # Try Kerberos auth
        pkg_info, clientauth, sec_buffer = self.init_sspi(scheme, request)
        self.try_kerberos(request, scheme, pkg_info, clientauth, sec_buffer)
        response = yield request
        if response.status_code != 401:
            final = response.headers.get("www-authenticate")
            if final is not None:
                try:
                    final = final.replace(scheme, '', 1).lstrip()
                    tokenbuf = win32security.PySecBufferType(
                        pkg_info['MaxToken'],
                        sspicon.SECBUFFER_TOKEN
                    )
                    tokenbuf.Buffer = base64.b64decode(final.encode('ASCII'))
                    sec_buffer.append(tokenbuf)
                    error, _ = clientauth.authorize(sec_buffer)
                    self.logger.debug(
                        "Kerberos Authentication succeeded - error=%s authenticated=%s",
                        error, clientauth.authenticated
                    )
                except TypeError:
                    pass
            return
        # Kerberos failed, to NTLM
        self.try_ntlm(request, response, scheme, pkg_info, clientauth, sec_buffer)
        yield request

    def init_sspi(
        self,
        scheme: str,
        request: Request
    ) -> Tuple[
            win32security.QuerySecurityPackageInfo,
            sspi.ClientAuth,
            win32security.PySecBufferDescType
        ]:
        if self.host is None:
            self.host = request.headers['host']
            try:
                self.host = socket.getaddrinfo(
                    self.host, None, 0, 0, 0, socket.AI_CANONNAME
                )[0][3]
                request.headers["host"] = self.host
            except socket.gaierror as err:
                self.logger.info(
                    'Skipping canonicalization of name %s due to error: %r',
                    self._host,
                    err
                )
        targetspn = '{}/{}'.format(self.service, self.host)
        scflags = sspicon.ISC_REQ_MUTUAL_AUTH
        if self.delegate:
            scflags |= sspicon.ISC_REQ_DELEGATE
        pkg_info = win32security.QuerySecurityPackageInfo(scheme)
        clientauth = sspi.ClientAuth(
            scheme,
            targetspn=targetspn,
            auth_info=self._auth_info,
            scflags=scflags,
            datarep=sspicon.SECURITY_NETWORK_DREP
        )
        sec_buffer = win32security.PySecBufferDescType()
        return pkg_info, clientauth, sec_buffer

    def try_kerberos(
        self,
        request: Request,
        scheme: str,
        pkg_info: win32security.QuerySecurityPackageInfo,
        clientauth: sspi.ClientAuth,
        sec_buffer: win32security.PySecBufferDescType,
    ) -> None:
        peercert = self.connection.peercert_b
        if peercert is not None:
            md = hashlib.sha256()
            md.update(peercert)
            appdata = 'tls-server-end-point:'.encode('ASCII') + md.digest()
            self.logger.debug("Channel binding hash %s", appdata)
            cbtbuf = win32security.PySecBufferType(
                pkg_info['MaxToken'], sspicon.SECBUFFER_CHANNEL_BINDINGS
            )
            cbtbuf.Buffer = struct.pack(
                'LLLLLLLL{}s'.format(len(appdata)),
                0, 0, 0, 0, 0, 0,
                len(appdata),
                32,
                appdata
            )
            sec_buffer.append(cbtbuf)
        
        try:
            error, auth = clientauth.authorize(sec_buffer)
            auth_header = f"{scheme} {base64.b64encode(auth[0].Buffer).decode('ASCII')}"
            request.headers["authorization"] = auth_header
            self.logger.debug(
                'Sending Initial Context Token - error=%s authenticated=%s',
                error,
                clientauth.authenticated
            )
        except pywintypes.error as err:
            self.logger.debug("Error in client auth: %r", repr(err))
            raise err
        return

    def try_ntlm(
        self,
        request: Request,
        response: H11Response,
        scheme: str,
        pkg_info: win32security.QuerySecurityPackageInfo,
        clientauth: sspi.ClientAuth,
        sec_buffer: win32security.PySecBufferDescType
    ) -> None:
        challenge_header = response.headers["www-authenticate"]
        challenge = [
            val[len(scheme)+1:] for val in challenge_header.split(', ') if scheme in val
        ]
        if len(challenge) > 1:
            raise ValueError(f"Did not get exactly one {scheme} challenge from server.")
        
        tokenbuf = win32security.PySecBufferType(
            pkg_info['MaxToken'],
            sspicon.SECBUFFER_TOKEN
        )
        tokenbuf.Buffer = base64.b64decode(challenge[0])
        sec_buffer.append(tokenbuf)
        self.logger.debug('Got Challenge Token (NTLM)')
        try:
            error, auth = clientauth.authorize(sec_buffer)
            auth_header = f"{scheme} {base64.b64encode(auth[0].Buffer).decode('ASCII')}"
            request.headers["authorization"] = auth_header
            self.logger.debug(
                'Sending challenge response - error=%s authenticated=%s',
                error,
                clientauth.authenticated
            )
        except pywintypes.error as err:
            self.logger.debug("Error in client auth: %r", repr(err))
            raise err
        if response.headers.get("set-cookie") is not None:
            request.headers["cookie"] = response.headers["set-cookie"]
        return