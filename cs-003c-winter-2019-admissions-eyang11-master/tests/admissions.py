"""
Admissions unit tests.
"""
import unittest
from data.applications import Applications
from school.admissions import get


class TestAdmissions(unittest.TestCase):
    """
    Tests for Admissions.
    """
    def setUp(self):
        self.applicants = Applications(1000)

    def test_duplicate(self):
        """
        check the admitted and wait_listed have no duplicate ids
        """
        admitted, wait_listed = get(self.applicants)
        check = True
        for admit in admitted:
            for wait in wait_listed:
                if admit.get("application_id") is wait.get("application_id"):
                    check = False
        self.assertTrue(check)

    def test_alumni_affirmative(self):
        """
        check the admitted's first 6 applicant has alumni parent and 7~9 have
        affirmative action
        """
        admitted, _ = get(self.applicants)
        check = True
        for index in range(6):
            if not admitted[index].get("has_alumni_parent"):
                check = False
        for index in range(3):
            if not admitted[index+6].get("affirmative_action"):
                check = False
        self.assertTrue(check)

if __name__ == "__main__":
    unittest.main()
