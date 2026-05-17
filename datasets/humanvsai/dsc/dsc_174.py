from packaging.version import Version

def from_protobuf(cls, proto):
    """
    Constructor from protobuf. Can raise ValueErrors from called from_protobuf() parsers.

    :param cls: class object
    :type cls: class
    :param proto: protobuf structure
    :type proto: ~unidown.plugin.protobuf.save_state_pb2.SaveStateProto
    :return: the SaveState
    :rtype: ~unidown.plugin.save_state.SaveState
    :raises ValueError: version of SaveState does not exist or is empty inside the protobuf
    :raises ~packaging.version.InvalidVersion: version is not PEP440 conform
    """
    # Your code here