def evidence_random_noise_prior(evidence, type_probs, subtype_probs):
    if evidence in subtype_probs:
        return subtype_probs[evidence]
    else:
        return type_probs[evidence]