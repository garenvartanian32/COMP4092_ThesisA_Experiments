def validate_quiz_access_code(self, id, course_id, access_code):
    quiz = self.get_quiz_by_id(id, course_id)
    if quiz is None:
        return False
    return quiz.access_code == access_code