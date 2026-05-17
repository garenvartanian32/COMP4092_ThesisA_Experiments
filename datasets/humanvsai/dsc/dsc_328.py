def evidence_random_noise_prior(evidence, type_probs, subtype_probs):
    # Check if the evidence corresponds to a subtype
    if evidence in subtype_probs:
        # If it does, return the curated prior noise probability for that subtype
        return subtype_probs[evidence]
    else:
        # If it doesn't, return the random-noise prior for the overall rule type
        return type_probs