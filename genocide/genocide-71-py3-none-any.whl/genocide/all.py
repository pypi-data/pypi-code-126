# This file is placed in the Public Domain.


import genocide.basic as basic
import genocide.model as model
import genocide.irc as irc
import genocide.rss as rss


from genocide.handler import Table


Table.add(basic)
Table.add(model)
Table.add(irc)
Table.add(rss)
