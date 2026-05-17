def formula(input):
    if input == "ATOM":
        return True
    elif input == "TRUE":
        return True
    elif input == "FALSE":
        return False
    else:
        raise ValueError("Invalid input, please provide ATOM or TRUE or FALSE")
