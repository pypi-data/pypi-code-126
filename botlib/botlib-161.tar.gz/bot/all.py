# This file is placed in the Public Domain.


import bot.bsc as bsc
import bot.irc as irc
import bot.rss as rss


from bot.hdl import Table


Table.add(bsc)
Table.add(irc)
Table.add(rss)
