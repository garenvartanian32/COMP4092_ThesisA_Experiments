def run(self, executable, memory_map):
    """
    Run a quil executable. If the executable contains declared parameters, then a memory
    map must be provided, which defines the runtime values of these parameters.

    :param executable: The program to run. You are responsible for compiling this first.
    :param memory_map: The mapping of declared parameters to their values. The values
        are a list of floats or integers.
    :return: A numpy array of shape (trials, len(ro-register)) that contains 0s and 1s.
    """
    # Your code here