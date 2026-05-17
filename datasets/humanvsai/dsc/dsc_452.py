class Validator:
    def __init__(self):
        self.validators = []

    def validator(self, meth):
        self.validators.append(meth)
        return meth

# Usage
validator = Validator()

@validator.validator
def validate_name(name):
    if not name:
        return "Name is required"

@validator.validator
def validate_age(age):
    if age < 18:
        return "You must be at least 18 years old"

# Now you can run the validators
for validator in validator.validators:
    print(validator("John"))
    print(validator(17))