def is_supported(self, target):
        if target.lower() not in self.targets_mcu_list:
            logging.debug("Target not found in definitions")
            return False
        mcu_record = self.targets.get_mcu_record(target) if self.mcus.get_mcu_record(target) is None else self.mcus.get_mcu_record(target)
        # Look at tool specific options which define tools supported for target
        # TODO: we might create a list of what tool requires
        if self.tool:
            # tool_specific requested look for it
            try:
                for k,v in mcu_record['tool_specific'].items():
                    if k == self.tool:
                        return True
            except (TypeError, KeyError) as err:
                pass
            return False
        else:
            # supports generic part (mcu part)
            return True