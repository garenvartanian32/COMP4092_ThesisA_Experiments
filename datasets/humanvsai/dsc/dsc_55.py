def mock(name):
    """Setup properties indicating status of name mock.

    This is designed to decorate ``torment.TestContext`` methods and is used to
    provide a consistent interface for determining if name is mocked once and
    only once.

    Parameters
    ----------
    name : str
        symbol in context's module to mock

    Return Value(s)
    ---------------
    bool
        True if name is mocked; otherwise, False.  Also, creates a property on the
        method's self, is_mocked_name, with this value.
    """
    # Your code here to mock the name and set the property