# -*- coding: utf-8 -*-
import os
import sys
import time
import json
import argparse
import logging

class BookmarkedTerminalCommands:
    FAIL = "\033[91m"
    OK_GREEN = "\033[92m"
    OK_CYAN = "\033[96m"
    ORANGE = "\033[93m"
    BOLD = "\033[1m"

    def __init__(self):
        self.work_folder = os.path.expanduser("~") + "/.favcmd/"
        self.store_file = self.work_folder + "store.json"

    def get_arguments(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-l", action="store_true")
        parser.add_argument("-s", "--save", dest="save", help="Save a command")
        parser.add_argument("-d", "--delete", dest="delete", help="Delete a command")
        parser.add_argument("-n", "--nick", dest="nick", help="Nick of the command")
        parser.add_argument("-r", "--run", dest="run", help="Run a command by the nick")
        options = parser.parse_args()
        if options.save and options.delete:
            parser.error(
                self.FAIL
                + self.BOLD
                + "[-] Please specify only one command per time to save or delete, use --help for more info."
            )
        if options.run and (options.save or options.delete):
            parser.error(
                self.FAIL
                + self.BOLD
                + "[-] Please specify the nick of command to run and not use in this case the -d and -s, use --help for more info."
            )
        return options

    def setup_temp_files(self):
        if not os.path.isdir(self.work_folder):
            os.mkdir(self.work_folder)
        if not os.path.isfile(self.store_file):
            os.system("echo '{}' > " + self.store_file)
            self.script_header()

    def load_favorites(self):
        with open(self.store_file, "r") as file:
            data = file.read()
        return json.loads(data)

    def set_favorite(self, nick, command, favorites):
        if nick and nick not in favorites:
            favorites[nick] = command
            print(self.OK_CYAN + "[+] New command saved.")
            print(self.OK_GREEN + "nick: " + nick + ", command: " + command)
        elif nick and nick in favorites:
            print(
                self.FAIL
                + self.BOLD
                + "[-] Please specify a new nick for this command, use --help for more info."
            )
        else:
            letters = ""
            for word in command.split():
                letters = letters + word[0]
            autoNick = "".join(letters).upper()
            self.set_favorite(autoNick, command, favorites)

    def save_favorite(self, options):
        favorites = self.load_favorites()
        self.set_favorite(options.nick, options.save, favorites)

        with open(self.store_file, "w") as outfile:
            json.dump(favorites, outfile)

    def delete_favorite(self, options):
        favorites = self.load_favorites()
        if options.delete in favorites:
            print(self.OK_CYAN + "[+] Command deleted:")
            print(
                self.FAIL
                + "nick: "
                + options.delete
                + ", command: "
                + favorites[options.delete]
            )
            del favorites[options.delete]
            with open(self.store_file, "w") as outfile:
                json.dump(favorites, outfile)

    def show_favorites(self):
        swap = self.ORANGE
        favorites = self.load_favorites()
        print(self.OK_CYAN + "[+] Favorite commands:")
        for key in favorites.keys():
            swap = self.OK_GREEN if swap == self.ORANGE else self.ORANGE
            print(swap + "nick: " + key + ", command: " + favorites[key])

    def run_command(self, options):
        favorites = self.load_favorites()
        if options.run in favorites:
            os.system(favorites[options.run])
        else:
            print(
                self.FAIL
                + self.BOLD
                + "[-] Please specify a command to run by a --nick, use --help for more info."
            )

    def run(self, options):
        self.setup_temp_files()

        if options.run:
            self.run_command(options)
        elif options.save:
            self.save_favorite(options)
        elif options.delete:
            self.delete_favorite(options)
        if options.l:
            self.show_favorites()

    def slow_print(self, s):
        for c in s + "\n":
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.0 / 100)

    def script_header(self):
        # see: https://patorjk.com/software/taag/
        self.slow_print(
            """\033[1;31m \033[95m
        ╔═╗┌─┐┬  ┬┌─┐┬─┐┬┌┬┐┌─┐  ╔═╗┌─┐┌┬┐┌┬┐┌─┐┌┐┌┌┬┐┌─┐
        ╠╣ ├─┤└┐┌┘│ │├┬┘│ │ ├┤   ║  │ │││││││├─┤│││ ││└─┐
        ╚  ┴ ┴ └┘ └─┘┴└─┴ ┴ └─┘  ╚═╝└─┘┴ ┴┴ ┴┴ ┴┘└┘─┴┘└─┘\033[92m
        """
        )


def main():
    favorite_commands_manager = BookmarkedTerminalCommands()
    options = favorite_commands_manager.get_arguments()
    favorite_commands_manager.run(options)


if __name__ == "__main__":
    main()
