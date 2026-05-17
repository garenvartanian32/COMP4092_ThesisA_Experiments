def _list_function_infos(jvm):
    """
    Returns a list of function information via JVM. Sorts wrapped expression infos by name
    and returns them.
    """

    jinfos = jvm.org.apache.spark.sql.api.python.PythonSQLUtils.listBuiltinFunctionInfos()
    infos = []
    for jinfo in jinfos:
        name = jinfo.getName()
        usage = jinfo.getUsage()
        usage = usage.replace("_FUNC_", name) if usage is not None else usage
        infos.append(ExpressionInfo(
            className=jinfo.getClassName(),
            name=name,
            usage=usage,
            arguments=jinfo.getArguments().replace("_FUNC_", name),
            examples=jinfo.getExamples().replace("_FUNC_", name),
            note=jinfo.getNote(),
            since=jinfo.getSince(),
            deprecated=jinfo.getDeprecated()))
    return sorted(infos, key=lambda i: i.name)