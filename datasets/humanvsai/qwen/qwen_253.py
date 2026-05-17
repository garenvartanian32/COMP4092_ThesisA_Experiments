def _build_volume(self, volume):
    volumes = []
    for v in volume:
        if 'hostPath' in v:
            volumes.append({'name': v.get('name'), 'hostPath': {'path': v.get('hostPath'), 'type': v.get('type', 'Directory')}})
        elif 'emptyDir' in v:
            volumes.append({'name': v.get('name'), 'emptyDir': {'medium': v.get('medium', '')}})
        elif 'configMap' in v:
            volumes.append({'name': v.get('name'), 'configMap': {'name': v.get('configMap'), 'items': v.get('items', [])}})
        elif 'secret' in v:
            volumes.append({'name': v.get('name'), 'secret': {'secretName': v.get('secret'), 'items': v.get('items', [])}})
        elif 'persistentVolumeClaim' in v:
            volumes.append({'name': v.get('name'), 'persistentVolumeClaim': {'claimName': v.get('claimName')}})
        else:
            raise ValueError(f'Unsupported volume type: {v}')
    return volumes