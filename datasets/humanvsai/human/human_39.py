def set_status(self, name: str = None):
        game = None
        if name:
            game = {
                'name': name
            }
        payload = {
            'op': WebSocketEvent.STATUS_UPDATE.value,
            'd': {
                'game': game,
                'status': 'online',
                'afk': False,
                'since': 0.0
            }
        }
        data = json.dumps(payload, indent=2)
        self.logger.debug(f'Sending status update payload: {data}')
        self._ws.send(data)