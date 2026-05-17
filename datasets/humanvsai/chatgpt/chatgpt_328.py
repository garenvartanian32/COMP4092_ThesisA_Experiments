def determine_prior_prob(evidence, subtype_dict, rule_type_dict):
    if evidence in subtype_dict:
        return subtype_dict[evidence]
    return rule_type_dict.get('random_noise_prior_prob', None)
