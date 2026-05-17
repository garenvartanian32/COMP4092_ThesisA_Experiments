def _classify_arithmetic(self, regs_init, regs_fini, mem_fini, written_regs, read_regs):
        matches = []
        # TODO: Review these restrictions.
        op_restrictions = {
            "+": lambda x, y: False,
            "-": lambda x, y: x == y,
            "|": lambda x, y: x == y,
            "&": lambda x, y: x == y,
            "^": lambda x, y: x == y,
        }
        # Check for "dst_reg <- src1_reg OP src2_reg" pattern.
        for op_name, op_fn in self._binary_ops.items():
            for src_1_reg, src_1_val in regs_init.items():
                # Make sure the *src* register was read.
                if src_1_reg not in read_regs:
                    continue
                for src_2_reg, src_2_val in regs_init.items():
                    # Make sure the *src* register was read.
                    if src_2_reg not in read_regs:
                        continue
                    for dst_reg, dst_val in regs_fini.items():
                        # Make sure the *dst* register was written.
                        if dst_reg not in written_regs:
                            continue
                        # Check restrictions.
                        if self._arch_regs_size[src_1_reg] != self._arch_regs_size[src_2_reg] or \
                            self._arch_regs_size[src_1_reg] != self._arch_regs_size[dst_reg]:
                            continue
                        # Avoid trivial operations.
                        if op_restrictions[op_name](src_1_reg, src_2_reg):
                            continue
                        size = self._arch_regs_size[src_1_reg]
                        if dst_val == op_fn(src_1_val, src_2_val) & (2**size - 1):
                            src = sorted([src_1_reg, src_2_reg])
                            src_ir = [
                                ReilRegisterOperand(src[0], self._arch_regs_size[src[0]]),
                                ReilRegisterOperand(src[1], self._arch_regs_size[src[1]])
                            ]
                            dst_reg_ir = ReilRegisterOperand(dst_reg, self._arch_regs_size[dst_reg])
                            matches.append({
                                "src": src_ir,
                                "dst": [dst_reg_ir],
                                "op":  op_name
                            })
        return matches