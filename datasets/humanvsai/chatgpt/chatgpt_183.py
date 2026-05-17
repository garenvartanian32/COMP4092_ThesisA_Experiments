def get_namespace_sequence(namespace: str, block_height: int, include_expired: bool = False) -> List[str]:
    # Get the relevant namespace record at the given block height
    namespace_record = get_namespace_record(namespace, block_height)
    
    # If the namespace record doesn't exist at the given block height, return an empty list
    if namespace_record is None:
        return []
    
    # Get the sequence of states that the namespace record was in at the given block height
    sequence = namespace_record.get_sequence(include_expired)
    
    # Return the sequence as a list of state IDs
    return [state.id for state in sequence]
