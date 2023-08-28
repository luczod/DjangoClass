def is_positive_number(valueInput):
    try:
        number_string = float(valueInput)
    except Exception as e:
        print(e)
        return False
    return number_string > 0
