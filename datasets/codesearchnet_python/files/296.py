def generate_sql_markdown(jvm, path):
    """
    Generates a markdown file after listing the function information. The output file
    is created in `path`.

    Expected output:
    ### NAME

    USAGE

    **Arguments:**

    ARGUMENTS

    **Examples:**

    ```
    EXAMPLES
    ```

    **Note:**

    NOTE

    **Since:** SINCE

    **Deprecated:**

    DEPRECATED

    <br/>

    """

    with open(path, 'w') as mdfile:
        for info in _list_function_infos(jvm):
            name = info.name
            usage = _make_pretty_usage(info.usage)
            arguments = _make_pretty_arguments(info.arguments)
            examples = _make_pretty_examples(info.examples)
            note = _make_pretty_note(info.note)
            since = info.since
            deprecated = _make_pretty_deprecated(info.deprecated)

            mdfile.write("### %s\n\n" % name)
            if usage is not None:
                mdfile.write("%s\n\n" % usage.strip())
            if arguments is not None:
                mdfile.write(arguments)
            if examples is not None:
                mdfile.write(examples)
            if note is not None:
                mdfile.write(note)
            if since is not None and since != "":
                mdfile.write("**Since:** %s\n\n" % since.strip())
            if deprecated is not None:
                mdfile.write(deprecated)
            mdfile.write("<br/>\n\n")