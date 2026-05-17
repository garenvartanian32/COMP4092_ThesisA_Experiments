def write_jobfile(self, task, **kwargs):
        script = self.qadapter.get_script_str(
            job_name=task.name,
            launch_dir=task.workdir,
            executable=task.executable,
            qout_path=task.qout_file.path,
            qerr_path=task.qerr_file.path,
            stdin=task.files_file.path,
            stdout=task.log_file.path,
            stderr=task.stderr_file.path,
            exec_args=kwargs.pop("exec_args", []),
        )
        # Write the script.
        with open(task.job_file.path, "w") as fh:
            fh.write(script)
            task.job_file.chmod(0o740)
            return task.job_file.path