#!/user/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
        print("{} {} {}".format(a, b, result))
    except ZeroDivisionError:
        print("its not alllwo for you div by zero")
    finally:
        print("we are done thanks ")
