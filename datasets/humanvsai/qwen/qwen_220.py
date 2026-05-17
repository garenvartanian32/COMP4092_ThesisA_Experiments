def FALSE(classical_reg):
    return MOVE(classical_reg, 0)

def TRUE(classical_reg):
    """Produce a TRUE instruction.

    :param classical_reg: A classical register to modify.
    :return: An instruction object representing the equivalent MOVE."""
    return MOVE(classical_reg, 1)

def NOT(classical_reg):
    """Produce a NOT instruction.

    :param classical_reg: A classical register to modify.
    :return: An instruction object representing the equivalent XOR."""
    return XOR(classical_reg, 1)

def AND(classical_reg, classical_reg2):
    """Produce an AND instruction.

    :param classical_reg: A classical register to modify.
    :param classical_reg2: A second classical register to use in the AND operation.
    :return: An instruction object representing the equivalent AND."""
    return AND(classical_reg, classical_reg2)

def OR(classical_reg, classical_reg2):
    """Produce an OR instruction.

    :param classical_reg: A classical register to modify.
    :param classical_reg2: A second classical register to use in the OR operation.
    :return: An instruction object representing the equivalent OR."""
    return OR(classical_reg, classical_reg2)

def XOR(classical_reg, classical_reg2):
    """Produce an XOR instruction.

    :param classical_reg: A classical register to modify.
    :param classical_reg2: A second classical register to use in the XOR operation.
    :return: An instruction object representing the equivalent XOR."""
    return XOR(classical_reg, classical_reg2)