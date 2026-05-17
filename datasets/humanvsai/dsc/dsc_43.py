import numpy as np

def get_compliance_expansion(elastic_tensor_expansion):
    compliance_tensor_expansion = []
    for tensor in elastic_tensor_expansion:
        compliance_tensor_expansion.append(np.linalg.inv(tensor))
    return compliance_tensor_expansion