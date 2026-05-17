def get_lan_members(self, datacenter_id, lan_id, depth=1):
    response = self._send_request(method='GET', path=f'/datacenters/{datacenter_id}/lans/{lan_id}/nics', depth=depth)
    return response.json()