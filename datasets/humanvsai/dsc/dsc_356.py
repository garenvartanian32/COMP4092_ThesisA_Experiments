class AdminService:
    def __init__(self, injector_gear):
        self.injector_gear = injector_gear

    def start_gear(self):
        self.injector_gear.start()

    def stop_gear(self):
        self.injector_gear.stop()

def make_admin_on_demand_service(injector_gear):
    return AdminService(injector_gear)