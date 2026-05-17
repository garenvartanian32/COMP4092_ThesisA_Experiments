def create_env_reaction(resource, deplete_resource=False):
    depletion = '' if not deplete_resource else '-'
    task = resource.replace('res', '').replace('0', '')
    return f'{resource} = gdspy.Path([(-10,-20),(10,-20)], 1).rotate(numpy.pi/2).translate((10,20))\nenv.add_reaction("{task}", {resource}, {depletion}1)'