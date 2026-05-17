def reset(self):
        # Can only reset tasks that are done.
        # One should be able to reset 'Submitted' tasks (sometimes, they are not in the queue
        # and we want to restart them)
        #if self.status != self.S_SUB and self.status < self.S_DONE: return 1
        # Remove output files otherwise the EventParser will think the job is still running
        self.output_file.remove()
        self.log_file.remove()
        self.stderr_file.remove()
        self.start_lockfile.remove()
        self.qerr_file.remove()
        self.qout_file.remove()
        if self.mpiabort_file.exists:
            self.mpiabort_file.remove()
        self.set_status(self.S_INIT, msg="Reset on %s" % time.asctime())
        self.num_restarts = 0
        self.set_qjob(None)
        # Reset finalized flags.
        self.work.finalized = False
        self.flow.finalized = False
        return 0