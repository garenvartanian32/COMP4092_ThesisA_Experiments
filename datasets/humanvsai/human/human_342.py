def _get_all_cwlkeys(items, default_keys=None):
    if default_keys:
        default_keys = set(default_keys)
    else:
        default_keys = set(["metadata__batch", "config__algorithm__validate",
                            "config__algorithm__validate_regions",
                            "config__algorithm__validate_regions_merged",
                            "config__algorithm__variant_regions",
                            "validate__summary",
                            "validate__tp", "validate__fp", "validate__fn",
                            "config__algorithm__coverage", "config__algorithm__coverage_merged",
                            "genome_resources__variation__cosmic", "genome_resources__variation__dbsnp",
                            "genome_resources__variation__clinvar"
        ])
    all_keys = set([])
    for data in items:
        all_keys.update(set(data["cwl_keys"]))
    all_keys.update(default_keys)
    return all_keys