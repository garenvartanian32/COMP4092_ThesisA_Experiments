def get_requirements() -> List[str]:
    return ['numpy', 'pandas', 'matplotlib', 'scikit-learn']

def install_requirements(requirements: List[str]) -> None:
    """Install the given requirements using pip."""
    for requirement in requirements:
        subprocess.run(['pip', 'install', requirement], check=True)

def main() -> None:
    requirements = get_requirements()
    install_requirements(requirements)