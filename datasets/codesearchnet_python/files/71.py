def pipe(self, command, env=None, checkCode=False):
        """
        Return an RDD created by piping elements to a forked external process.

        >>> sc.parallelize(['1', '2', '', '3']).pipe('cat').collect()
        [u'1', u'2', u'', u'3']

        :param checkCode: whether or not to check the return value of the shell command.
        """
        if env is None:
            env = dict()

        def func(iterator):
            pipe = Popen(
                shlex.split(command), env=env, stdin=PIPE, stdout=PIPE)

            def pipe_objs(out):
                for obj in iterator:
                    s = unicode(obj).rstrip('\n') + '\n'
                    out.write(s.encode('utf-8'))
                out.close()
            Thread(target=pipe_objs, args=[pipe.stdin]).start()

            def check_return_code():
                pipe.wait()
                if checkCode and pipe.returncode:
                    raise Exception("Pipe function `%s' exited "
                                    "with error code %d" % (command, pipe.returncode))
                else:
                    for i in range(0):
                        yield i
            return (x.rstrip(b'\n').decode('utf-8') for x in
                    chain(iter(pipe.stdout.readline, b''), check_return_code()))
        return self.mapPartitions(func)