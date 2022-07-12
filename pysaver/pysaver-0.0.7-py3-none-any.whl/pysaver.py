"""repl_saver.py - Save python repl history."""
import readline
from datetime import datetime


# REPL history saved:
# 2022-07-10T00:00:18.809794

def sublist(lst1, lst2):
   ls1 = [element for element in lst1 if element in lst2]
   ls2 = [element for element in lst2 if element in lst1]
   return ls1 == ls2


def comment_blank_remove_line(lines):
    return [line for line in lines if line and line[0]!="\n" and line[0]!="#"]


def check_previous_save(filename):
    """Checks if file exists."""
    try:
        with open(filename, "r") as f:
            lines = f.read().split("\n")
            lines = comment_blank_remove_line(lines)
    except FileNotFoundError:
        with open(filename, "wt") as f:
            f.write("")
            lines = []

    return lines


def repl_history(num_lines=-1, file_name="saved_repl_history.py"):
    """repl_history(num_lines, file_name)
    
    Saves python repl history to file_name."""
    total = readline.get_current_history_length()

    if num_lines == -1:
        # default value prints everything
        num_lines = total

    if num_lines > 0:
        # range from n->end in order to incl. recent line
        with open(file_name, "at") as f:
            f.write("\n# Session beginning:")
            f.write("\n# " + datetime.now().isoformat())
            for i in range(total - num_lines, total):
                f.write(readline.get_history_item(i + 1)+"\n")
            f.write("\n")


repl_history()
