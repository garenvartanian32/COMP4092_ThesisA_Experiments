def source_setattr():

    def setter(self, value):
        self.source = {self.context.key: value}
    return setter

class MyClass:

    def __init__(self, context):
        self.context = context
        self.source = {}
        setattr(self, 'value', property(fset=source_setattr()))
context = {'key': 'example_key'}
obj = MyClass(context)
obj.value = 10