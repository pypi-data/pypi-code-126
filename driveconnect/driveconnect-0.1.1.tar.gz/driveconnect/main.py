import ctypes
import platform
import string
import subprocess
import pysecstring as pss

def cmd(cmd):
    '''
    Run a command in cmd.exe and return its value.
    '''
    return subprocess.call(cmd, shell=True)

def compress(data, selectors):
    for d, s in zip(data, selectors):
        if s:
            yield d

def get_available_drives():
    # nice solution from: https://stackoverflow.com/questions/4188326/in-python-how-do-i-check-if-a-drive-exists-w-o-throwing-an-error-for-removable
    if 'Windows' not in platform.system():
        return []
    drive_bitmask = ctypes.cdll.kernel32.GetLogicalDrives()
    return list(compress(string.ascii_uppercase,
                         map(lambda x: ord(x) - ord('0'),
                             bin(drive_bitmask)[:1:-1])))

def is_drive_connected(drive_letter):
    return drive_letter.rstrip(':') in get_available_drives()

# https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/gg651155(v=ws.11)
# https://discuss.dizzycoding.com/what-is-the-best-way-to-map-windows-drives-using-python/
# the first possibility

def _connect_drive(drive_letter, server_path, username, password):
    cmd_ = f"net use {drive_letter.rstrip(':')}: \\\\{server_path.lstrip('\\')} /user:{username} {password}"
    # print(cmd_)
    return cmd(cmd_)

def _disconnect_drive(drive_letter):
    cmd_ = f"net use {drive_letter.rstrip(':')}: /del"
    # print(cmd_)
    return cmd(cmd_)

def connect_drive(drive_letter, server_path, user_file=None, pass_file=None):
    if not is_drive_connected(drive_letter):
        if user_file is None and pass_file is None:
            cmd_ = f"net use {drive_letter}: \\\\{server_path.lstrip('\\')}"
            # print(cmd_)
            cmd(cmd_)
        else:
            co = pss.get_credentials(user_file, pass_file)
            _connect_drive(drive_letter, server_path, co.username, co.password)
        print(f"{server_path} successfully connected to {drive_letter.rstrip(':')}:")

def disconnect_drive(drive_letter):
    if is_drive_connected(drive_letter.rstrip(':')):
        _disconnect_drive(drive_letter.rstrip(':'))