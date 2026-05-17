def set_exec_area(self, exec_area):
        yield from self._hypervisor.send('vm set_exec_area "{name}" {exec_area}'.format(name=self._name,
                                                                                        exec_area=exec_area))
        log.info('Router "{name}" [{id}]: exec area updated from {old_exec}MB to {new_exec}MB'.format(name=self._name,
                                                                                                      id=self._id,
                                                                                                      old_exec=self._exec_area,
                                                                                                      new_exec=exec_area))
        self._exec_area = exec_area