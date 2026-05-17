def from_protobuf(cls, proto):
    version = proto.version
    if not version:
        raise ValueError('version of SaveState is empty inside the protobuf')
    try:
        version = Version(version)
    except InvalidVersion:
        raise InvalidVersion(f'version {version} is not PEP440 conform')
    return cls(version=version, **other_params)