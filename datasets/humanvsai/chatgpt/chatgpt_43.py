def compliance_tensor_expansion(elastic_tensor_expansion):
    """
    Gets a compliance tensor expansion from the elastic tensor expansion.
    
    Parameters:
    elastic_tensor_expansion (list): A 6x6 array representing the elastic tensor expansion.
    
    Returns:
    list: A 6x6 array representing the compliance tensor expansion.
    """
    compliance_tensor_expansion = [[0]*6 for _ in range(6)]
    for i in range(6):
        for j in range(6):
            if i == j:
                compliance_tensor_expansion[i][j] = 1/elastic_tensor_expansion[i][j]
            else:
                compliance_tensor_expansion[i][j] = \
                    -elastic_tensor_expansion[i][j]/(elastic_tensor_expansion[i][i]*elastic_tensor_expansion[j][j] - \
                    elastic_tensor_expansion[i][j]*elastic_tensor_expansion[j][i])
    return compliance_tensor_expansion
