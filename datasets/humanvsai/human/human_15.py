def check_hamster(self):
        try:
            # can't use the client because then we end up in a dbus loop
            # as this is initiated in storage
            todays_facts = self.storage._Storage__get_todays_facts()
            self.check_user(todays_facts)
        except Exception as e:
            logger.error("Error while refreshing: %s" % e)
        finally:  # we want to go on no matter what, so in case of any error we find out about it sooner
            return True