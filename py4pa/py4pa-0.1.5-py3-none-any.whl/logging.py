from datetime import datetime as datetime

class Log_File:
    """Python class to enable logging of key events to a file of your choosing, 
    as well as the console if you wish

    Parameters
    ----------
    directory : str
        The file location where you want the output file saved, 
        excluding the file name

    fName : str (optional)
        The filename, including extension that you want to use as your output.
        If this isn't specified, the file will be called 'progress_log - YYYY-MM-DD HH:MM:SS.txt', 
        where the date & time stamp will be the time when the log is first initiated.

    print_to_console : bool (optional)
        Defaults to True. If set to true, will print messages to both the log file, 
        and the console. If False, will only output to the log file    
    """


    def __init__(self, directory, fName=None, print_to_console=True):

        self.run_date_time = datetime.now().strftime('%Y-%m-%d T%H:%M:%S')
        self.fName = f'progress_log - {self.run_date_time}.txt'

        if fName is not None:
            self.fName = fName

        self.fPath = f'{directory}/{self.fName}'

        self.print_to_console = print_to_console

    def add_section(self, section_title):
        """Adds a section heading to the log output

        Parameters
        ----------
        section_title : str
            The title you wish to add to the log output
        
        """
        with open(self.fPath, 'a') as f:
            f.write('##############################' + '\n')
            f.write(section_title.center(30))
            f.write('##############################' + '\n')

        if self.print_to_console:
            print(f'##############################')
            print(section_title.center(30))
            print(f'##############################')


    def log(self, status):
        """Adds a time-stamped status update to the log file & console

        Parameters
        ----------
        
        status : str
            The text of the status update you wish to add. The method will add 
            the date and time stamp automatically.
        
        """
        now = datetime.now().strftime('%Y-%m-%d T%H:%M:%S - ')
        
        with open(self.fPath, 'a') as f:
                f.write(now + status + '\n')

        if self.print_to_console:
            print(f'{now}{status}')


def continuous_logging(msg):
    """Function to print out messages that over-write each other as a new message is sent

    Parameters
    ----------
    msg: String
        the message to be printed to the console

    Returns
    -------
    None
    """

    print(f'\r{msg}\r', end='', flush=True)

    return None