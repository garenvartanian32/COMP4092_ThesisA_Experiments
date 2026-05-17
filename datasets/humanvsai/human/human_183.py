def namedb_get_namespace_at(cur, namespace_id, block_number, include_expired=False):
    if not include_expired:
        # don't return anything if the namespace was expired at this block.
        # (but do return something here even if the namespace was created after this block, so we can potentially pick up its preorder (hence only_revealed=False))
        namespace_rec = namedb_get_namespace(cur, namespace_id, block_number, include_expired=False, include_history=False, only_revealed=False)
        if namespace_rec is None:
            # expired at this block
            return None
    history_rows = namedb_get_record_states_at(cur, namespace_id, block_number)
    if len(history_rows) == 0:
        # doesn't exist yet 
        return None
    else:
        return history_rows