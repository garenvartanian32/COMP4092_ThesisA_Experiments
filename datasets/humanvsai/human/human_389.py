def links(base_dir: str, issuer_did: str = None) -> set:
        LOGGER.debug('Tails.links >>> base_dir: %s, issuer_did: %s', base_dir, issuer_did)
        if issuer_did and not ok_did(issuer_did):
            LOGGER.debug('Tails.links <!< Bad DID %s', issuer_did)
            raise BadIdentifier('Bad DID {}'.format(issuer_did))
        rv = set()
        for dir_path, dir_names, file_names in walk(base_dir, topdown=True):
            dir_names[:] = [d for d in dir_names if not d.startswith('.')]
            for file_name in file_names:
                if islink(join(dir_path, file_name)) and (not issuer_did or ok_rev_reg_id(file_name, issuer_did)):
                    rv.add(join(dir_path, file_name))
        LOGGER.debug('Tails.links <<< %s', rv)
        return rv