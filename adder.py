import sys

def add_values(values):
    if len(values) == 0:
        return None
    try:
        result = 0
        for value in values:
            value_as_number = 0
            try:
                value_as_number = int(value)
            except ValueError:
                value_as_number = float(value)
            result += value_as_number
    except ValueError:
        result = ""
        for value in values:
            result += value
    return result


if __name__ == "__main__":
    result = add_values(sys.argv[1:])
    print(result)
