class PackageSpecification:
    def __init__(self, contents):
        self.contents = contents

def mk_package(contents):
    """Instantiates a package specification from a parsed "AST" of a
    package.

    Parameters
    ----------
    contents : dict

    Returns
    ----------
    PackageSpecification
    """
    return PackageSpecification(contents)