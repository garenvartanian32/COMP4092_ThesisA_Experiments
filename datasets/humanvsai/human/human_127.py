def get_config(self):
        if 'rmq_port' in self.config:
            self.rmq_port = int(self.config['rmq_port'])
        if 'rmq_user' in self.config:
            self.rmq_user = self.config['rmq_user']
        if 'rmq_password' in self.config:
            self.rmq_password = self.config['rmq_password']
        if 'rmq_vhost' in self.config:
            self.rmq_vhost = self.config['rmq_vhost']
        if 'rmq_exchange_type' in self.config:
            self.rmq_exchange_type = self.config['rmq_exchange_type']
        if 'rmq_durable' in self.config:
            self.rmq_durable = bool(self.config['rmq_durable'])
        if 'rmq_heartbeat_interval' in self.config:
            self.rmq_heartbeat_interval = int(
                self.config['rmq_heartbeat_interval'])