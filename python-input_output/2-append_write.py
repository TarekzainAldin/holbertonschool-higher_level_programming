#!/user/bin/python3
"""append write"""


def append_write(filename="", text=""):
    """append the string at the end of text file utf-8"""
    lenght = 0
    with open(filename, "a") as f:
        lenght = f.write(text)
        f.close()
    return lenght
