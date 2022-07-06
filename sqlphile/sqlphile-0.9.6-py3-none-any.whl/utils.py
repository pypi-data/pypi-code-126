import datetime
import time
from .d import D
from .f import F
import re

def toD (dict, engine):
    d = D (**dict)
    d.encode (engine)
    return d

def make_orders (order_by, keyword = "ORDER"):
    if isinstance (order_by, str):
        order_by = [order_by]
    orders = []
    for f in order_by:
        f = str (f)
        if f.find ("-") != -1:
            orders.append (f.replace ("-", '') + " DESC")
        elif f.find ("+") != -1:
            orders.append (f.replace ("+", ''))
        else:
            orders.append (f)
    return "{} BY {}".format (keyword, ", ".join (orders))

def mkdatetime (unixtime):
    return datetime.datetime.utcfromtimestamp (unixtime)

ENDING = re.compile (r"[.,\s]")
def omit (data, limit = 50):
    if len (data) < limit:
        return data
    m = ENDING.search (data, limit - 10)
    if m:
        data = data [:m.start ()].strip ()
        if len (data) <= (limit - 3):
            return data + "..."
    return data [:limit - 3].strip () + "..."

def as_dict (conn, row):
    fields = [x.name for x in conn.description]
    return dict ([(f, _row [i]) for i, f in enumerate (fields)])

def csv_row (row, line_delim = "", encoding = None):
    d = []
    for cell in row:
        if isinstance (cell, str):
            d.append ('"{}"'.format (cell.replace ('"', '\"')))
        elif isinstance (cell, datetime.datetime):
            d.append (cell.strftime ("%Y-%m-%d %H:%M:%S"))
        elif cell is None:
            d.append ('""')
        else:
            d.append (str (cell))
    row = "{}{}".format (",".join (d), line_delim)
    if encoding:
        row = row.encode (encoding)
    return row

