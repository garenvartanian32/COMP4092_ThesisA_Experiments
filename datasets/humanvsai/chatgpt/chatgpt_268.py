def check_and_format(data):
    result, messages = data.check()
    return result.value, messages