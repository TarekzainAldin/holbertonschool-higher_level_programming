#!/user/bin/python3
def safe__print_integer(valu):
    try:
        print("{:d}".format(value))
    except Exception:
        return False
    return True
