def _assemble_influence(stmt):
    subj_str = _assemble_agent_str(stmt.subj.concept)
    obj_str = _assemble_agent_str(stmt.obj.concept)
    # Note that n is prepended to increase to make it "an increase"
    if stmt.subj.delta['polarity'] is not None:
        subj_delta_str = ' decrease' if stmt.subj.delta['polarity'] == -1 \
            else 'n increase'
        subj_str = 'a%s in %s' % (subj_delta_str, subj_str)
    if stmt.obj.delta['polarity'] is not None:
        obj_delta_str = ' decrease' if stmt.obj.delta['polarity'] == -1 \
            else 'n increase'
        obj_str = 'a%s in %s' % (obj_delta_str, obj_str)
    stmt_str = '%s causes %s' % (subj_str, obj_str)
    return _make_sentence(stmt_str)