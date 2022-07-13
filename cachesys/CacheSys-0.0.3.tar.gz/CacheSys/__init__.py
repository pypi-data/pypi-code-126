def WriteCache(name=str, content=str, dst=any):
    """
    name = File name (include extension),
    content = Contents to put in the file,
    dst = File destination
    """

    from os.path import exists
    import os

    check_path = os.path.exists(f"{dst}")

    if check_path == False:
        os.makedirs(f"{dst}")

    a = open(f"{dst}/{name}", "w")

    a.write(f"{content}")

    a.close()

    del os
    del exists

    return 0

def ReadCache(name=str, src=any):
    """
    name = File name (include extension),
    src = File location (do not include the file name)
    """

    a = open(f"{src}/{name}", "r")

    b = a.read()

    a.close()

    return b