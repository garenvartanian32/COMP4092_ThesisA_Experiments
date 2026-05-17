def evidence_random_noise_prior(evidence, type_probs, subtype_probs):
    (stype, subtype) = tag_evidence_subtype(evidence)
    # Get the subtype, if available
    # Return the subtype random noise prior, if available
    if subtype_probs is not None:
        if stype in subtype_probs:
            if subtype in subtype_probs[stype]:
                return subtype_probs[stype][subtype]
    # Fallback to just returning the overall evidence type random noise prior
    return type_probs[stype]