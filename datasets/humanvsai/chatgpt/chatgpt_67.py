def map_resnum_to_seqnum(resnums, structprop, chain_id, seqprop, use_representatives=False):
    if use_representatives:
        seqprop = SeqProp.load_representative()
        structprop = StructProp.load_representative()
        chain_id = structprop.get_representative_chain()
    mapping_dict = {}
    for resnum in resnums:
        residue = structprop.get_residue(resnum, chain_id)
        seqnum = seqprop.get_resnum_from_ident(residue.ident)
        mapping_dict[resnum] = seqnum
    return mapping_dict