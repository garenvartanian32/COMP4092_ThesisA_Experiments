def guess_sequence(redeem_script):
    import re
    pattern = '(\\d+)\\s+OP_CSV'
    match = re.search(pattern, redeem_script)
    if match:
        sequence = int(match.group(1))
        return sequence
    else:
        return 4294967295
redeem_script = '100 OP_CSV'
redeem_script = 'OP_CSV'
redeem_script = '100 OP_CHECKSEQUENCEVERIFY'
redeem_script = 'OP_CHECKSEQUENCEVERIFY'