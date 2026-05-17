def validator_decorator(meth):
    validators.append(meth)
    return meth
