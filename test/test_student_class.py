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


if __name__ == '__main__':
    unittest.main()
