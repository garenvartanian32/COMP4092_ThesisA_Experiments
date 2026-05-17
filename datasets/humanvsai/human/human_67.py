def map_structprop_resnums_to_seqprop_resnums(self, resnums, structprop=None, chain_id=None, seqprop=None,
                                                  use_representatives=False):
        resnums = ssbio.utils.force_list(resnums)
        if use_representatives:
            seqprop = self.representative_sequence
            structprop = self.representative_structure
            chain_id = self.representative_chain
            if not structprop:
                raise ValueError('No representative structure set, please specify sequence, structure, and chain ID')
        else:
            if not seqprop or not structprop or not chain_id:
                raise ValueError('Please specify sequence, structure, and chain ID')
        if structprop.id == self.representative_structure.id:
            full_structure_id = '{}-{}'.format(structprop.id, chain_id).replace('REP-', '')
        else:
            full_structure_id = '{}-{}'.format(structprop.id, chain_id)
        aln_id = '{}_{}'.format(seqprop.id, full_structure_id)
        access_key = '{}_chain_index'.format(aln_id)
        if access_key not in seqprop.letter_annotations:
            raise KeyError(
                '{}: structure mapping {} not available in sequence letter annotations. Was alignment parsed? '
                'Run ``align_seqprop_to_structprop`` with ``parse=True``.'.format(access_key, aln_id))
        chain = structprop.chains.get_by_id(chain_id)
        chain_structure_resnum_mapping = chain.seq_record.letter_annotations['structure_resnums']
        final_mapping = {}
        for resnum in resnums:
            resnum = int(resnum)
            resnum_index = chain_structure_resnum_mapping.index(resnum)
            struct_res_singleaa = structprop.chains.get_by_id(chain_id).seq_record[resnum_index]
            # if resnum not in seqprop.letter_annotations[access_key]:
            #     log.warning('{}-{} -> {}: unable to map residue {} from structure to sequence, '
            #                 'skipping'.format(structprop.id, chain_id, seqprop.id, resnum))
            #     continue
            what = seqprop.letter_annotations[access_key].index(resnum_index+1)
            # TODO in progress...
            seq_res_singleaa = seqprop[what]
            sp_resnum = what + 1
            final_mapping[resnum] = sp_resnum
            # Additionally report if residues are the same - they could be different in the structure though
            format_data = {'seqprop_id'       : seqprop.id,
                           'seqprop_resid'    : seq_res_singleaa,
                           'seqprop_resnum'   : sp_resnum,
                           'structprop_id'    : structprop.id,
                           'structprop_chid'  : chain_id,
                           'structprop_resid' : struct_res_singleaa,
                           'structprop_resnum': resnum}
            if struct_res_singleaa != seq_res_singleaa:
                log.warning('Sequence {seqprop_id} residue {seqprop_resid}{seqprop_resnum} does not match to '
                            'structure {structprop_id}-{structprop_chid} residue '
                            '{structprop_resid}{structprop_resnum}. NOTE: this may be due to '
                            'structural differences'.format(**format_data))
            else:
                log.debug('Sequence {seqprop_id} residue {seqprop_resid}{seqprop_resnum} is mapped to '
                          'structure {structprop_id}-{structprop_chid} residue '
                          '{structprop_resid}{structprop_resnum}'.format(**format_data))
        return final_mapping