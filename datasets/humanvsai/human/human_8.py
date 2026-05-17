def data32_send(self, type, len, data, force_mavlink1=False):
                return self.send(self.data32_encode(type, len, data), force_mavlink1=force_mavlink1)