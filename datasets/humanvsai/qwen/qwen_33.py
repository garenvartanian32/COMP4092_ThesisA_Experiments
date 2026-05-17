def get_diagnosis(self, remediation_id=None):
    try:
        if remediation_id:
            response = self.client.get(f'/diagnosis/{remediation_id}')
        else:
            response = self.client.get('/diagnosis')
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f'Error fetching diagnosis data: {e}')
        return None