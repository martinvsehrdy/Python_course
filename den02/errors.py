
def function(a, b):
    if a > 20:
        raise ValueError("I dont like number greater than 20")
    return a / b


if __name__ == '__main__':
    try:
        result = function(23, 0)
    except ValueError as e:
        print("Value Error", e)
    except ZeroDivisionError as e:
        print("Zero Division Error", str(e))
    except Exception as e:
        print("Exception", str(e))
    else:
        print("result is", result)
    finally:
        print("executing finally clause")

