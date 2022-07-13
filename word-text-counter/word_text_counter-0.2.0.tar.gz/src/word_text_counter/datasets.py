from importlib import resources

def get_flatland_path() -> str:
    """get sample text file path, with name "flatland.txt".

    Returns:
        str: a flatland.txt path.
    """

    with resources.path("word_text_counter.data","flatland.txt") as fp:
        file_path = fp
    return str(file_path)


def get_time_machine_path() -> str:
    """get sample text file path, with name "time_machine.txt".

    Returns:
        str: a time_machine.txt path.
    """
    
    with resources.path("word_text_counter.data","time_machine.txt") as fp:
        file_path = fp
    return str(file_path)