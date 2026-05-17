from typing import List
from restclients.models import Curriculum, Department

def get_curriculum_for_department(department: Department) -> List[Curriculum]:
    """
    Returns a list of restclients.Curriculum models, for the passed Department model.
    """
    curriculums = Curriculum.objects.filter(department=department)
    return list(curriculums)
