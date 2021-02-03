"""
Get admissions.
"""
from data.applications import Applications
from school import admissions
import random

class Run(object):
    """
    Invoking the admissions logic.
    """
    random.seed(0)
    applicants = Applications(1000)
    applicants_list, admitted, wait_listed = [], [], []
    for apply in applicants:
        applicants_list.append(apply)
    admitted, wait_listed = admissions.get(applicants_list)
    def print_list(self):
        """
        Print admitted and waitlisted candidate details.
        """
        sort_admitted = sorted(self.admitted, key=lambda x: x.get("application_id"))
        sort_waited = sorted(self.wait_listed, key=lambda x: x.get("application_id"))
        for index, applicant in enumerate(sort_admitted):
            print(index+1, applicant.get("application_id"))
        for index, applicant in enumerate(sort_waited):
            print(index+1, applicant.get("application_id"))

if __name__ == "__main__":
    Run().print_list()
