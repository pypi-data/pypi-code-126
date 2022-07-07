#  =============================================================================
#  GNU Lesser General Public License (LGPL)
#
#  Copyright (c) 2022 Qujamlee from www.aztquant.com
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#  =============================================================================
from ._quote_api_base import *


class QuoteApi(QuoteApiBase):
    def Subscribe(self, codes, sync=False, timeout=None):
        return self._subscribe(codes, sync=sync, timeout=timeout)

    def Unsubscribe(self, codes, sync=False, timeout=None):
        return self._unsubscribe(codes, sync=sync, timeout=timeout)

    def Start(self, server_addr: str, spi=None, timeout=None):
        return self._start(server_addr, spi, timeout)

    def Stop(self):
        return self._stop()  # 正常stop返回None

    def Join(self, timeout=None):
        self._join(timeout=timeout)
