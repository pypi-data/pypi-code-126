# **************************************************************************** #
#                           This file is part of:                              #
#                                BITSMITHS                                     #
#                           https://bitsmiths.co.za                            #
# **************************************************************************** #
#  Copyright (C) 2015 - 2022 Bitsmiths (Pty) Ltd.  All rights reserved.        #
#   * https://bitbucket.org/bitsmiths_za/bitsmiths                             #
#                                                                              #
#  Permission is hereby granted, free of charge, to any person obtaining a     #
#  copy of this software and associated documentation files (the "Software"),  #
#  to deal in the Software without restriction, including without limitation   #
#  the rights to use, copy, modify, merge, publish, distribute, sublicense,    #
#  and/or sell copies of the Software, and to permit persons to whom the       #
#  Software is furnished to do so, subject to the following conditions:        #
#                                                                              #
#  The above copyright notice and this permission notice shall be included in  #
#  all copies or substantial portions of the Software.                         #
#                                                                              #
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  #
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,    #
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL     #
#  THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER  #
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING     #
#  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER         #
#  DEALINGS IN THE SOFTWARE.                                                   #
# **************************************************************************** #

import datetime

import bs_audit

from bs_lib import query_builder
from bs_lib import PodAsync


class TableWatchAsync:
    """
    This object sets up a watch on an interval of your choice. If table/s that
    you are watching change, you will be notified when changes have occured.
    """

    def __init__(self, pod: PodAsync, dao_name: str, watch_list: list = None, interval: int = 0):
        """
        Constructor.

        :param pod: The pod object to use.
        :param dao_name: Name of dao module to use.
        :param watch_list: The table watch list, if none, then all tables are watched.
        :param interval: How many seconds wait before checking for changes.
        """
        self._pod       = pod
        self._dao       = bs_audit.dao_by_name(dao_name, 'dao_async')
        self.watch_list = watch_list or []
        self.interval   = interval
        self.last_check = datetime.datetime.min
        self.next_check = datetime.datetime.min


    def __del__(self):
        """
        Destructor.
        """
        pass


    async def get_changed(self, watch_list: list = None, from_check_time: datetime.datetime = None) -> list:
        """
        Gets all the tables that have had changes since the last time
        that you made this method call.

        :param watch_list: Optionally give a custom watch list to check.
        :param from_check_time: Override the lastCheck time, and check from here instead.
        :return: A list of table id's that have changed, None if nothing has changed.
        """
        if from_check_time is None:
            dtnow = datetime.datetime.now()

            if dtnow < self.next_check:
                return []

            self.last_check = dtnow

            if self.interval > 0:
                self.next_check = dtnow + datetime.timedelta(seconds=self.interval)
            else:
                self.next_check = dtnow

        qry = self._dao.dCfgChangedSince(self._pod.dbcon)
        qry.irec.since = from_check_time or self.last_check

        if watch_list or self.watch_list:
            qry.irec.crit += query_builder(watch_list, 'c', 'id')

        res = []

        await qry.exec()

        while await qry.fetch():
            res.append(qry.orec.id)

        return res
