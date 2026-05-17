def guess_sequence(redeem_script):
    try:
        script_array = redeem_script.split()
        loc = script_array.index('OP_CHECKSEQUENCEVERIFY')
        return int(script_array[loc - 1], 16)
    except ValueError:
        return 0xFFFFFFFE