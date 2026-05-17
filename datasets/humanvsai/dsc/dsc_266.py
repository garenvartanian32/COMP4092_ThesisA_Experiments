class MyClass:
    def send_message(self, *args, **kwargs):
        """Wrapped method would accept new `queued` and `isgroup`
        OPTIONAL arguments"""
        queued = kwargs.get('queued', None)
        isgroup = kwargs.get('isgroup', None)

        # Now you can use queued and isgroup as you need
        if queued is not None:
            print(f"Queued: {queued}")
        if isgroup is not None:
            print(f"IsGroup: {isgroup}")

# Usage
my_object = MyClass()
my_object.send_message(queued=True, isgroup=False)