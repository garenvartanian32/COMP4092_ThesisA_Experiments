import json

class Diagnosis:
    def __init__(self):
        self.diagnosis_data = {
            "diagnosis1": {"id": 1, "name": "Diagnosis 1"},
            "diagnosis2": {"id": 2, "name": "Diagnosis 2"},
            # Add more diagnosis data as needed
        }

    def get_diagnosis(self, remediation_id=None):
        if remediation_id is None:
            return json.dumps(self.diagnosis_data)
        else:
            if remediation_id in self.diagnosis_data:
                return json.dumps(self.diagnosis_data[remediation_id])
            else:
                return None