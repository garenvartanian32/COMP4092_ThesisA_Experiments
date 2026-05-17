def parse(s):
        """
        Parse string representation back into the SparseVector.

        >>> SparseVector.parse(' (4, [0,1 ],[ 4.0,5.0] )')
        SparseVector(4, {0: 4.0, 1: 5.0})
        """
        start = s.find('(')
        if start == -1:
            raise ValueError("Tuple should start with '('")
        end = s.find(')')
        if end == -1:
            raise ValueError("Tuple should end with ')'")
        s = s[start + 1: end].strip()

        size = s[: s.find(',')]
        try:
            size = int(size)
        except ValueError:
            raise ValueError("Cannot parse size %s." % size)

        ind_start = s.find('[')
        if ind_start == -1:
            raise ValueError("Indices array should start with '['.")
        ind_end = s.find(']')
        if ind_end == -1:
            raise ValueError("Indices array should end with ']'")
        new_s = s[ind_start + 1: ind_end]
        ind_list = new_s.split(',')
        try:
            indices = [int(ind) for ind in ind_list if ind]
        except ValueError:
            raise ValueError("Unable to parse indices from %s." % new_s)
        s = s[ind_end + 1:].strip()

        val_start = s.find('[')
        if val_start == -1:
            raise ValueError("Values array should start with '['.")
        val_end = s.find(']')
        if val_end == -1:
            raise ValueError("Values array should end with ']'.")
        val_list = s[val_start + 1: val_end].split(',')
        try:
            values = [float(val) for val in val_list if val]
        except ValueError:
            raise ValueError("Unable to parse values from %s." % s)
        return SparseVector(size, indices, values)