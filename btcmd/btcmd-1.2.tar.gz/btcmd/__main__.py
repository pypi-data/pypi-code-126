from btcmd.btcmd import BookmarkedTerminalCommands

def main():
    favorite_commands_manager = BookmarkedTerminalCommands()
    options = favorite_commands_manager.get_arguments()
    favorite_commands_manager.run(options)


if __name__ == "__main__":
    main()