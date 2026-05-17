def get_lan_members(self, datacenter_id, lan_id, depth=1):
        response = self._perform_request(
            '/datacenters/%s/lans/%s/nics?depth=%s' % (
                datacenter_id,
                lan_id,
                str(depth)))
        return response