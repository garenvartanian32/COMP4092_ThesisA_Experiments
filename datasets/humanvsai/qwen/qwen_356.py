def make_admin_on_demand_service(injector_gear):
    admin_service = AdminService(injector_gear)
    return admin_service

class AdminService:

    def __init__(self, gear):
        self.gear = gear

    def start(self):
        """Start the linked gear."""
        self.gear.start()

    def stop(self):
        """Stop the linked gear."""
        self.gear.stop()