def validate_quiz_access_code(self, id, course_id, access_code):
    """Validate quiz access code.

    Accepts an access code and returns a boolean indicating whether that access code is correct"""

    # Assume we have a function get_access_code(id, course_id) that retrieves the correct access code from the database
    correct_access_code = self.get_access_code(id, course_id)

    return access_code == correct_access_code