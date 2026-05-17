def _check_range_minions(self, expr, greedy):
    if not expr:
        return []
    if expr.startswith('G@'):
        return self._check_grain(expr[2:], greedy)
    elif expr.startswith('I@'):
        return self._check_pillar(expr[2:], greedy)
    elif expr.startswith('L@'):
        return self._check_list(expr[2:], greedy)
    elif expr.startswith('E@'):
        return self._check_pcre(expr[2:], greedy)
    elif expr.startswith('J@'):
        return self._check_jid(expr[2:], greedy)
    elif expr.startswith('S@'):
        return self._check_ipcidr(expr[2:], greedy)
    elif expr.startswith('P@'):
        return self._check_pillar_exact(expr[2:], greedy)
    elif expr.startswith('N@'):
        return self._check_nodegroup(expr[2:], greedy)
    elif expr.startswith('R@'):
        return self._check_range(expr[2:], greedy)
    elif expr.startswith('X@'):
        return self._check_exsel(expr[2:], greedy)
    elif expr.startswith('RO@'):
        return self._check_reap(expr[2:], greedy)
    elif expr.startswith('LO@'):
        return self._check_lrange(expr[2:], greedy)
    elif expr.startswith('NO@'):
        return self._check_nrange(expr[2:], greedy)
    elif expr.startswith('C@'):
        return self._check_compound(expr[2:], greedy)
    elif expr.startswith('LC@'):
        return self._check_listcompound(expr[2:], greedy)
    elif expr.startswith('GLOB@'):
        return self._check_glob(expr[2:], greedy)
    else:
        return self._check_list(expr, greedy)