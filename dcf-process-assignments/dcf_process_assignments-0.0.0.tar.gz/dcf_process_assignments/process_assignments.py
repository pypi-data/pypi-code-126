# DCF dcf_process_assignments package; main package functionality
# process_assignments.py: main package functionality
# Author: Mubarak Idoko (midoko.dev@gmail.com)
# Date: 06/19/2022

# UPDATE LOG
# Format: (Name of author) Date: Note
# (Mubarak Idoko) earlier date before logging: Wrote the script and implemented all functionality
# (Mubarak Idoko) 06/19/2022: Fixed the date issue with the script

# KNOWN ISSUES:
# Format: (Name of author) Date [Critical Score (0-5)]: Notes [Ideas for fix] {Updates (if any)}
# (Mubarak Idoko) 06/19/2022: 0:
    # Limited to year in the 2000's so by 2100...
    # this code will still work, but is technically not correct

##### INFO #####
# process_assignment.py
#
# python script to that reads a *.csv file containing DCF Assignment Data as a string
# and a *.csv file containing a list of people making videos for this assignment as a string 
# and the date for the assignment as a string, in the form "mar-1-22" for March 1st, 2022 

# For the assignment file, make sure that:
#   1. These headings exist exactly: "Entity ID Display", "Pref Name Sort", "Entity Pref Class Year", "Email Pref Address", "Salutation", "DCF Segment Desc"

# For the people making videos file, make sure that:
#   1. These headings exist exactly: "Student Name", "Class Year", "Email"

# create a directory with the data string e.g. "mar-1-22" in assignments/sends and assignments/campaigns
# and for each student making videos for the week, writes an excel file in the form:
#               "studentFirstName_date_sends.xlsx" in the assignments/sends/date directory
#           and "studentFirstName_date.xlsx" in the assignments/campaigns/date directory

# Author: Mubarak Idoko, March 22


##### IMPORTS #####
import os
import sys
import re
from datetime import datetime, date
import argparse
from argparse import RawTextHelpFormatter
import pandas as pd

##### CONSTANTS #####
PARENT_DIR_ASSIGNMENTS_SENDS = "/assignments/sends/"
PARENT_DIR_ASSIGNMENTS_CAMPAIGNS ="/assignments/campaigns/"
ASSIGNMENT_FILE_HEADINGS = ["Entity ID Display", "Pref Name Sort",
                              "Entity Pref Class Year", "Email Pref Address",
                              "Salutation", "DCF Segment Desc"]
FINAL_FILE_HEADINGS = ["Donor ID", "Last Name", "Class Year", "Email", "First Name", "Category"]
SEND_FILE_HEADINGS = ["Last Name", "Class Year", "First Name", "Category"]
PPLE_MAKING_VIDEOS_HEADINGS = ["Student Name", "Class Year", "Email"]
PPLE_NAME_HEADING = PPLE_MAKING_VIDEOS_HEADINGS[0]
SEND = "_send"
CAMPAIGN = "_campaign"
LOGGING = True
EXCEL_EXTENSION = ".xlsx"


##### FUNCTIONS #####
# ============== log_processing ==============
def log_processing(message):
    """print log messages to stdout if LOGGING flag is set 
    """
    if LOGGING:
        print("LOG:", message)

def log_error(message):
    """print error messages  
    """
    if LOGGING:
        print("ERROR:", message)

# ============== make_assignment_dirs ==============
def make_assignment_dirs(input_date: str) -> tuple:
    """ Makes directory to store assignment files
        Would exception if the parentDir is invalid 

    Parameters
    ---------
    input_date : str
        The date of the assignment in the form "mar-1-22"
        that is "mon-DD-YY"
    Return
    ------
        Tuple containing the paths to the "send" directory and "campaign" directory
    """
    parent_path = os.path.dirname(os.getcwd())
    path_segments = re.split(r"\\|\/", parent_path) # split by the directories
    if path_segments[-1] != "DCF Thankview":
        parent_path += "/DCF Thankview"

    # send
    path_send = parent_path + PARENT_DIR_ASSIGNMENTS_SENDS
    path_send = os.path.join(path_send, input_date + "/")

    # campaign
    path_campaign = parent_path + PARENT_DIR_ASSIGNMENTS_CAMPAIGNS
    path_campaign = os.path.join(path_campaign, input_date + "/")

    # make dirs
    if not os.path.exists(path_send):
        os.mkdir(path_send)
        log_processing("Created directory " + path_send)
    else:
        log_processing(path_send + " already exists")
    if not os.path.exists(path_campaign):
        os.mkdir(path_campaign)
        log_processing("Created directory " + path_campaign)
    else:
        log_processing(path_campaign + " already exists")

    return path_send, path_campaign

# ============== validate_csv_extension ==============
def validate_csv_extension(csv_file_path: str):
    """Ensure that is given file that is expected to the *.csv is actually csv

    Args:
        csv_file_path (str): the path of the file in question as a string

    Raises:
        ValueError: Error raised if the file is not a valid csv file
    """
    if csv_file_path[-4:len(csv_file_path)] != ".csv":
        raise ValueError(csv_file_path + " is not a *.csv file")
    log_processing(csv_file_path + " is a valid *.csv file")

# ============== validate_date ==============
def validate_date(date_text: str):
    """ Validates a date string 
    Parameters
    ---------
    date_text: str
        A date string
    Note
    -----------
        -> Limited to year in the 2000's so by 2100... 
        -> this code will still work, but is technically not correct
    """
    # validate the year against the current year
    curr_year = int(str(date.today())[2:4])
    year_input = int(date_text.split("-")[2])
    if year_input > curr_year:
        log_error("Year, 20" + str(year_input) +
                  ", is in the future. Cannot process assignment"
                  "for a year that does not yet exits.\n"
                  "Script will end now.")
        raise ValueError("Year, 20" + str(year_input) + ", is in the future")

    datetime.strptime(date_text, '%b-%d-%y')
    log_processing(date_text + " is valid")


# ============== validate_input_files ==============
def validate_input_files(assignment_csv_path: str, pple_mkng_vids_csv: str) -> pd.DataFrame:
    """Validates the input files

    Parameters
    ---------
    assignment_csv_path: str
        path to csv file of assignments to validate
    pple_mkng_vids_csv: str
        path to csv file containing list of people making videos 

    Return
    ------
        -> pandas dataframes containing the date in the files as a tuple 
    """

    # validate extensions
    validate_csv_extension(assignment_csv_path)
    validate_csv_extension(pple_mkng_vids_csv)

    # try to open files
    try:
        assignment_data = pd.read_csv(assignment_csv_path, usecols=ASSIGNMENT_FILE_HEADINGS)
    except IOError as error:
        log_processing("Cannot open " + assignment_csv_path)
        log_error(error.strerror + ": " + assignment_csv_path)
        sys.exit(1)

    try:
        people_data = pd.read_csv(pple_mkng_vids_csv, usecols=PPLE_MAKING_VIDEOS_HEADINGS)
    except IOError as error:
        log_processing("Cannot open " + pple_mkng_vids_csv)
        log_error(error.strerror + ": " + pple_mkng_vids_csv)
        sys.exit(1)

    # rename column headings for assignment file
    assignment_data.columns = FINAL_FILE_HEADINGS

    # output dataframes
    return assignment_data, people_data

# ============== processAssignment ==============
def process_assignments(assignment_date: str, assignment_csv: str, pple_mkng_vids_csv: str):
    """ Main function to process the assignments
        Requires a single run to process everything

    Parameters:
    ----------
    assignment_date: str
        The date of the assignment in the form "mar-1-22"
        that is "mon-DD-YY"
    assignment_csv: str
        path to csv file containing the list for the assignments
    pple_mkng_vids_csv: str
        path to csv file containing a list of people making videos
        the format is:
            Student Name,Class Year,Email
            Mubarak Idoko,23,mubarak.o.idoko.23@dartmouth.edu
    """

    # validate arguments
    # ensure that argument are valid
    assert isinstance(assignment_date,
                      str), 'dcf_process_assignments(): parameter date = {} not of <class "str">'.format(
                          assignment_date)
    assert isinstance(assignment_csv,
                      str), 'dcf_process_assignments(): parameter assignment_csv = {} not of <class "str">'.format(
                          assignment_csv)
    assert isinstance(pple_mkng_vids_csv,
                      str), 'dcf_process_assignments(): parameter pple_mkng_vids_csv = {} not of <class "str">'.format(
                          pple_mkng_vids_csv)

    ## date: will break if date is invalid
    assignment_date = assignment_date.lower()
    validate_date(assignment_date)

    ## input files:
    # will break if files are not the correct path, do not exist, 
    # or do not contain the correct columns
    assignment_data, people_data = validate_input_files(assignment_csv, pple_mkng_vids_csv)

    # make output directories
    path_send, path_campaign = make_assignment_dirs(assignment_date)

    # process assignments
    # compute numbers
    num_making_vids = people_data.shape[0] # starts indexing from 0, i.e. in computer speak
    num_videos_to_make = assignment_data.shape[0]
    vids_per_person = num_videos_to_make // num_making_vids
    remaining_vids = num_videos_to_make % num_making_vids

    # make divisions
    bottom = 0
    top = vids_per_person
    buckets = []
    extra_index = 0
    while top <= num_videos_to_make:
        if (remaining_vids > 0 and extra_index < remaining_vids):
             buckets.append(assignment_data.iloc[bottom:top + 1])
             bottom += vids_per_person + 1
             top += vids_per_person + 1
             extra_index += 1
        else:
            buckets.append(assignment_data.iloc[bottom:top])
            bottom += vids_per_person
            top += vids_per_person

    #  save campaign and sends file for each person
    for index, row in people_data.iterrows():
        # variables
        current_frame = buckets[index]
        name = row[PPLE_NAME_HEADING].split(" ")[0]
        campaign_file_name = name + CAMPAIGN + "_" + assignment_date + EXCEL_EXTENSION
        send_file_name = name + SEND + "_" + assignment_date + EXCEL_EXTENSION

        # paths
        campaign_file_path = os.path.join(path_campaign, campaign_file_name)
        send_file_path = os.path.join(path_send, send_file_name)

        # export to excel
        current_frame.to_excel(campaign_file_path, index = False, header = True)
        log_processing("Wrote *" + EXCEL_EXTENSION
                       + " campaign file for " + name + " in " + campaign_file_name)
        current_frame.to_excel(send_file_path, 
                               index = False, header = True, columns = SEND_FILE_HEADINGS)
        log_processing("Wrote *" + EXCEL_EXTENSION
                       + " send file for " + name + " in " + send_file_path)


##### PARSE ARGUMENTS #####
description_string = f'''
description:
    Process Assignment given the date, *.csv assignment list, 
    and *.csv people making videos list
'''

help_string = f'''
additional information: 
    This program takes in the date for the assignment
    Formatted in the form "mar-20-22" for March 20, 2022

    It also reads two CSV Files.
    The first one contains the list for the assignment 
    Formatted with columns (exactly): 
    "Entity ID Display", "Pref Name Sort", "Entity Pref Class Year", 
    "Email Pref Address", "Salutation", "DCF Segment Desc",

    The second file contains a list of the people making videos for this assignment
    Formatted with columns (exactly):
    "Student Name", "Class Year", "Email"
    Where in the form: Mubarak Idoko,23,mubarak.o.idoko.23@dartmouth.edu
                    
    All of these have to be correct for it to work properly
'''

parser = argparse.ArgumentParser(
            prog="dcf_process_assignments.py",
            description=description_string,
            epilog=help_string,
            formatter_class=RawTextHelpFormatter
        )
parser.add_argument('--dateOfAssignment', '-d',
                    dest="date", type=str, required=True, help="date of assignment")
parser.add_argument('--assignment_csv', '-a',
                    dest="assignFile", type=str, required=True,
                    help="csv file with assignment list")
parser.add_argument('--makingVideosCSV', '-p',
                    dest="ppleFile", type=str, required=True,
                    help="csv file with list of people making videos")


# ###### MAIN #####
def main():
    """_summary_
        Main function to process the assignments
    """
    args = parser.parse_args()
    date_in = args.date
    assign_file = args.assignFile
    pple_file = args.ppleFile
    process_assignments(date_in, assign_file, pple_file)


if __name__ == '__main__':
    main()
    