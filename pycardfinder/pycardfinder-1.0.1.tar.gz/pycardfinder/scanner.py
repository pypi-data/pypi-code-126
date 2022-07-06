from datetime import datetime
from card_identifier.cardutils import format_card, validate_card
from card_identifier.card_type import identify_card_type
import logging
import os
import click

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def strip_specials(raw):
    return "".join(e for e in raw if e.isalnum())

def verify_card(card_number):
    """
    Check if card is valid using Luhn algorithim.
    Assumption: Card numbers are more than 14 digits
    """
    n_digits = len(card_number)
    if n_digits < 14:
        return False
    return validate_card(card_number)



total_files = 0
incidents = 0

def find_cards(folder, ignore_items = "venv,.pyc,.git,node_modules"):
    global total_files
    global incidents
    ignore_list = []
    if ignore_items:
        ignore_list = ignore_items.split(",")
    for file_item in os.listdir(folder):
        total_files = total_files + 1
        filepath = os.path.join(folder, file_item)
        if any(s in filepath for s in ignore_list):
            continue
        try:
            if os.path.isdir(filepath):
                find_cards(filepath, ignore_items)
            else:
                with open(filepath, 'r') as fp:
                    content = fp.readlines()
                    for line_number, row in enumerate(content):
                        for item in row.split(" "):
                            card = format_card(item)
                            if card not in strip_specials(item):
                                continue
                            if verify_card(card):
                                card_type = identify_card_type(card)
                                if card_type.lower() != "unknown":
                                    incidents = incidents+1
                                    print(f"{line_number} : {filepath} {item} - found {card} {card_type}")
        except (UnicodeDecodeError, OSError, FileNotFoundError) as ex:
            # Put focus on what can be read for now, ignore what is not readble
            pass
        except Exception as ex:
            logger.error(f"Error: {ex}", exc_info=True)

@click.command()
@click.option('--path', help='Folder or path to scan')
@click.option('--ignore_items', help='Comma separated list of files extensions or folders to skip during scan')
def scan(path, ignore_items = "venv,.pyc,.git,node_modules"):
    print("Starting card scan..")
    start_time = datetime.now()
    find_cards(path, ignore_items)
    end_time = datetime.now()
    time_taken = end_time-start_time
    time_taken_s = time_taken.seconds
    time_taken_m = int(time_taken_s/60)
    print("-------------------------------------------- Summary --------------------------------------------")
    print(f"Started on: {start_time}")
    print(f"Total number of files scanned: {total_files}")
    print(f"Number of cards found (incident): {incidents}")
    print(f"Ended at: {end_time}")
    print(f"Time taken: {time_taken_m}mins (={time_taken_s}s)")
    print("-------------------------------------------- End of report --------------------------------------------")
    print("Completed card scan")
