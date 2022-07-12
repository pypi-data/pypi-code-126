import logging


def log_line(line, buffer, level):
  if len(line) > 0:
    buffer.append(line)
  logging.log(level, f"{line}")
