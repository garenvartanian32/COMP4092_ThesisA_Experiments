def _build_volume(self, volume):
        self.volumes[self._build_volume_name(volume.get('host'))] = {
            'name': self._build_volume_name(volume.get('host')),
            'hostPath': {
                'path': volume.get('host')
            }
        }
        response = {
            'name': self._build_volume_name(volume.get('host')),
            'mountPath': volume.get('container'),
        }
        if volume.get('readonly', False):
            response['readOnly'] = bool(volume.get('readonly', False))
        return response