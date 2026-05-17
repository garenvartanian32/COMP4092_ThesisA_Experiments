def run_script(dist_spec, script_name):
    ns = sys._getframe(1).f_globals
    name = ns['__name__']
    ns.clear()
    ns['__name__'] = name
    require(dist_spec)[0].run_script(script_name, ns)