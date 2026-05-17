def get_compliance_expansion(self):
    compliance_tensor = np.linalg.inv(self.elastic_tensor)
    return compliance_tensor

def get_elastic_tensor(self):
    """Returns the elastic tensor."""
    return self.elastic_tensor

def get_compliance_tensor(self):
    """Returns the compliance tensor."""
    return self.elastic_tensor_inv

def set_elastic_tensor(self, elastic_tensor):
    """Sets the elastic tensor."""
    self.elastic_tensor = elastic_tensor
    self.elastic_tensor_inv = np.linalg.inv(elastic_tensor)

class Elasticity:

    def __init__(self, elastic_tensor):
        self.elastic_tensor = elastic_tensor
        self.elastic_tensor_inv = np.linalg.inv(elastic_tensor)

    def get_compliance_expansion(self):
        """Gets a compliance tensor expansion from the elastic
        tensor expansion."""
        compliance_tensor = np.linalg.inv(self.elastic_tensor)
        return compliance_tensor

    def get_elastic_tensor(self):
        """Returns the elastic tensor."""
        return self.elastic_tensor

    def get_compliance_tensor(self):
        """Returns the compliance tensor."""
        return self.elastic_tensor_inv

    def set_elastic_tensor(self, elastic_tensor):
        """Sets the elastic tensor."""
        self.elastic_tensor = elastic_tensor
        self.elastic_tensor_inv = np.linalg.inv(elastic_tensor)