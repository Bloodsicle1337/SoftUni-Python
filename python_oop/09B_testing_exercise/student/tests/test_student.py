import unittest

from project.student import Student


class StudentTests(unittest.TestCase):
    def setUp(self) -> None:
        self.student = Student("Peter")

    def test_initialization_with_no_courses(self) -> None:
        self.assertEqual("Peter", self.student.name)
        self.assertEqual({}, self.student.courses)

    def test_initialization_with_courses(self) -> None:
        courses = {
            "Python": ["OOP", "Testing"]
        }

        student = Student("George", courses)

        self.assertEqual("George", student.name)
        self.assertEqual(courses, student.courses)

    def test_enroll_existing_course_updates_notes(self) -> None:
        self.student.courses = {
            "Python": ["OOP"]
        }

        result = self.student.enroll(
            "Python",
            ["Testing", "Decorators"]
        )

        self.assertEqual(
            "Course already added. Notes have been updated.",
            result
        )
        self.assertEqual(
            ["OOP", "Testing", "Decorators"],
            self.student.courses["Python"]
        )

    def test_enroll_new_course_with_y_adds_course_and_notes(self) -> None:
        result = self.student.enroll(
            "Python",
            ["OOP", "Testing"],
            "Y"
        )

        self.assertEqual(
            "Course and course notes have been added.",
            result
        )
        self.assertEqual(
            ["OOP", "Testing"],
            self.student.courses["Python"]
        )

    def test_enroll_new_course_with_empty_option_adds_notes(self) -> None:
        result = self.student.enroll(
            "Python",
            ["OOP", "Testing"]
        )

        self.assertEqual(
            "Course and course notes have been added.",
            result
        )
        self.assertEqual(
            ["OOP", "Testing"],
            self.student.courses["Python"]
        )

    def test_enroll_new_course_without_notes_option(self) -> None:
        result = self.student.enroll(
            "Python",
            ["OOP", "Testing"],
            "N"
        )

        self.assertEqual(
            "Course has been added.",
            result
        )
        self.assertEqual([], self.student.courses["Python"])

    def test_add_notes_to_existing_course(self) -> None:
        self.student.courses = {
            "Python": ["OOP"]
        }

        result = self.student.add_notes(
            "Python",
            "Testing"
        )

        self.assertEqual("Notes have been updated", result)
        self.assertEqual(
            ["OOP", "Testing"],
            self.student.courses["Python"]
        )

    def test_add_notes_to_missing_course_raises_exception(self) -> None:
        with self.assertRaises(Exception) as error:
            self.student.add_notes(
                "Python",
                "Testing"
            )

        self.assertEqual(
            "Cannot add notes. Course not found.",
            str(error.exception)
        )

    def test_leave_existing_course_removes_it(self) -> None:
        self.student.courses = {
            "Python": ["OOP"],
            "Java": ["Basics"]
        }

        result = self.student.leave_course("Python")

        self.assertEqual("Course has been removed", result)
        self.assertNotIn("Python", self.student.courses)
        self.assertIn("Java", self.student.courses)

    def test_leave_missing_course_raises_exception(self) -> None:
        with self.assertRaises(Exception) as error:
            self.student.leave_course("Python")

        self.assertEqual(
            "Cannot remove course. Course not found.",
            str(error.exception)
        )


if __name__ == "__main__":
    unittest.main()