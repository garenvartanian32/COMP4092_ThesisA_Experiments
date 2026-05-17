from packaging.requirements import Requirement
from packaging.version import parse


def outdated_requirements(req_file: str, skip_packages: list) -> list:
    with open(req_file) as f:
        reqs = f.read().splitlines()

    outdated_reqs = []

    for req in reqs:
        if any(skip_pkg in req for skip_pkg in skip_packages):
            continue

        req_obj = Requirement(req)
        if req_obj.specifier.contains(parse(req_obj.specifier.version)):
            outdated_reqs.append(req)

    return outdated_reqs
