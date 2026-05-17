def make_admin_on_demand_service(injector_gear):
        LOGGER.debug("InjectorCachedGearService.make_admin_on_demand_service")
        args = {
            'service_q': injector_gear.id,
            'treatment_callback': injector_gear.admin,
            'service_name': injector_gear.id + " - On Demand Start/Stop Service"
        }
        return InjectorCachedGearService.driver.make_service(args)