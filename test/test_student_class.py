import unittest

from definitions import student_class as sc


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.student = sc.Student("Pfander", "Colten", "Computer Information Systems")

    def tearDown(self):
        del self.student

    def test_object_created_required_attributes(self):
        self.assertEqual(self.student.last_name, "Pfander")
        self.assertEqual(self.student.first_name, "Colten")
        self.assertEqual(self.student.major, "Computer Information Systems")
        self.assertEqual(self.student.gpa, 0.0)

    def test_initial_all_attributes(self):
        new_student = sc.Student("Anctil", "Abby", "History", 4.0)
        assert new_student.last_name == "Anctil"
        assert new_student.first_name == "Abby"
        assert new_student.major == "History"
        assert new_student.gpa == 4.0

    def test_student_str(self):
        self.assertEqual(str(self.student), "Pfander, Colten has major Computer Information Systems with gpa: 0.0")

    def test_object_not_created_error_last_name(self):
        with self.assertRaises(ValueError):
            s = sc.Student("123", "Colten", "Computer Information Systems", 3.5)

    def test_object_not_created_error_first_name(self):
        with self.assertRaises(ValueError):
            s = sc.Student("Colten", "123", "Computer Information Systems", 3.5)

    def test_object_not_created_error_major(self):
        with self.assertRaises(ValueError):
            s = sc.Student("Pfander", "Colten", "123", 3.5)

    def test_object_not_created_error_gpa(self):
        with self.assertRaises(ValueError):
            s = sc.Student("Pfander", "Colten", "Computer Information Systems", "hello")


if __name__ == '__main__':
    unittest.main()
