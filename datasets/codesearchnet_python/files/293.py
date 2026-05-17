def _make_pretty_examples(examples):
    """
    Makes the examples description pretty and returns a formatted string if `examples`
    starts with the example prefix. Otherwise, returns None.

    Expected input:

        Examples:
          > SELECT ...;
           ...
          > SELECT ...;
           ...

    Expected output:
    **Examples:**

    ```
    > SELECT ...;
     ...
    > SELECT ...;
     ...
    ```

    """

    if examples.startswith("\n    Examples:"):
        examples = "\n".join(map(lambda u: u[6:], examples.strip().split("\n")[1:]))
        return "**Examples:**\n\n```\n%s\n```\n\n" % examples