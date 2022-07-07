import logging
import cx_Oracle


class DbOracle:

  @staticmethod
  def connect(username=None,
              password=None,
              host=None,
              port=None,
              database=None,
              service=None):
    dsn = cx_Oracle.makedsn(host, port, service_name=database)
    return cx_Oracle.connect(username, password, dsn)

  @staticmethod
  def query(cursor, request, params=None, verbose=False):
    if verbose:
      logging.info(f"Request: {request}")
      logging.info(f"Params: {params}")
    if params is not None:
      cursor.execute(request, params)
    else:
      cursor.execute(request)
    try:
      rows = cursor.fetchall()
      if verbose:
        for row in rows:
          logging.info(f"{' | '.join([str(i) for i in row])}")
      return rows
    except cx_Oracle.InterfaceError:
      return list()
