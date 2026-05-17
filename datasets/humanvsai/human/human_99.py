def get_requirements() -> List[str]:
    requirements_path = os.path.join(
        os.path.dirname(__file__), 'requirements.txt'
    )
    with open(requirements_path) as f:
        return f.read().split()