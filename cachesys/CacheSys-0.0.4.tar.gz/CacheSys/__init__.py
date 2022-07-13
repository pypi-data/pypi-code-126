def WriteCache(name=str, content=str, dst=any):
    """
    name = File name (include extension),
    content = Contents to put in the file,
    dst = File destination
    """

    from os.path import exists
    import os

    slashes = {"/", "\\"}

    x = str(dst)

    z = x.endswith(str(slashes))

    if z == True:

        a = open(f"{dst}{name}", "w")

        a.write(f"{content}")

        a.close()

        del os
        del exists

        return 0

    else:
        
        a = open(f"{dst}\\{name}", "w")

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

    slashes = {"/", "\\"}

    x = str(src)

    z = x.endswith(str(slashes))

    if z == True:

        a = open(f"{src}{name}", "r")

        b = a.read()

        a.close()

        return b

    else:

        a = open(f"{src}\\{name}", "r")

        b = a.read()

        a.close()

        return b