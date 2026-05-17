def run_simulation(project_dir: str, xml_file: str) -> None:
    """
    Perform a HydPy workflow in agreement with the given XML configuration file available in the directory of the given
    project.

    Parameters
    ----------
    project_dir : str
        The directory of the project containing the XML configuration file.
    xml_file : str
        The name of the XML configuration file.

    Returns
    -------
    None

    """
    import os
    from hydpy import Project
    from hydpy.core import xmltools
    os.chdir(project_dir)
    setup = xmltools.fromxml(xml_file)
    with Project(setup) as project:
        project.simulate()
