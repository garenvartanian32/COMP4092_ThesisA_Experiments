def start_accepting_passive_svc_checks(self):
        # todo: #783 create a dedicated brok for global parameters
        if not self.my_conf.accept_passive_service_checks:
            self.my_conf.modified_attributes |= DICT_MODATTR["MODATTR_PASSIVE_CHECKS_ENABLED"].value
            self.my_conf.accept_passive_service_checks = True
            self.my_conf.explode_global_conf()
            self.daemon.update_program_status()