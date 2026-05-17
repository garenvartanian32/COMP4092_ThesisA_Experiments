def constructor_from_protobuf(proto):
    try:
        version_string = proto.version
        if not version_string:
            raise ValueError("version of SaveState does not exist or is empty inside the protobuf")
        version = packaging.version.parse(version_string)
    except packaging.version.InvalidVersion:
        raise
    except Exception as e:
        raise ValueError(str(e))

    return SaveState(version, data=proto.data)