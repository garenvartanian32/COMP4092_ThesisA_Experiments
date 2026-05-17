def _add_uid(self, uid, skip_handle=False):
        # We might add None values from wherever. Kill them here.
        uid = uid or ''
        if is_arxiv(uid):
            self._ensure_reference_field('arxiv_eprint', normalize_arxiv(uid))
        elif idutils.is_doi(uid):
            self._ensure_reference_field('dois', [])
            self.obj['reference']['dois'].append(idutils.normalize_doi(uid))
        elif idutils.is_handle(uid) and not skip_handle:
            self._ensure_reference_field('persistent_identifiers', [])
            self.obj['reference']['persistent_identifiers'].append({
                'schema': 'HDL',
                'value': idutils.normalize_handle(uid),
            })
        elif idutils.is_urn(uid):
            self._ensure_reference_field('persistent_identifiers', [])
            self.obj['reference']['persistent_identifiers'].append({
                'schema': 'URN',
                'value': uid,
            })
        elif self.RE_VALID_CNUM.match(uid):
            self._ensure_reference_field('publication_info', {})
            self.obj['reference']['publication_info']['cnum'] = uid
        elif is_cds_url(uid):
            self._ensure_reference_field('external_system_identifiers', [])
            self.obj['reference']['external_system_identifiers'].append({
                'schema': 'CDS',
                'value': extract_cds_id(uid),
            })
        elif is_ads_url(uid):
            self._ensure_reference_field('external_system_identifiers', [])
            self.obj['reference']['external_system_identifiers'].append({
                'schema': 'ADS',
                'value': extract_ads_id(uid),
            })
        else:
            # ``idutils.is_isbn`` is too strict in what it accepts.
            try:
                isbn = str(ISBN(uid))
                self._ensure_reference_field('isbn', {})
                self.obj['reference']['isbn'] = isbn
            except Exception:
                raise ValueError('Unrecognized uid type')