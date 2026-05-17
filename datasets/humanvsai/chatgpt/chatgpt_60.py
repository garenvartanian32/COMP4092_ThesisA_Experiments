def calculate_overlap_distance_matrix(seq_list):
    """
    Calculates values for the overlap distance matrix, stability within a sequence, and distinctness between sequences.
    These values are cached so that they do need to be recomputed for calls to each of several accessor methods that use these values.
    """
    overlap_matrix = []
    stability_list = []
    distinctness_list = []
    
    for idx, seq1 in enumerate(seq_list):
        overlap_row = []
        for seq2 in seq_list[:idx] + seq_list[idx+1:]:
            overlap = len(set(seq1) & set(seq2))
            overlap_row.append(overlap)
        overlap_matrix.append(overlap_row)
        
        stability = sum(overlap_row) / len(seq1)
        stability_list.append(stability)
        
    for i, seq1 in enumerate(seq_list):
        distinctness = sum([overlap_matrix[i][j] * stability_list[j] for j in range(len(seq_list)) if j != i]) / sum(overlap_matrix[i])
        distinctness_list.append(distinctness)
        
    return overlap_matrix, stability_list, distinctness_list
