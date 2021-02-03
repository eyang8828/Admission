"""
Admissions.
"""


def get(applications):
    """
    It's easier to do this step by step, first picking alumni/affirmative children as quotas permit
    and placing the rest in a general pool along with the others.
    """
    admitted, wait_listed = [], []
    sort_applications = sorted(applications,
                               key=lambda x: x.get("school_gpa")*1.25
                               +x.get("personal_statement_grade"),
                               reverse=True)
    alumni_list = []
    for index, applicant in enumerate(sort_applications):
        if applicant.get("has_alumni_parent") is True:
            alumni_list.append(index)
        if len(alumni_list) == 6:
            break
    for index, number in enumerate(alumni_list):
        admitted.append(sort_applications.pop(number-index))

    action_list = []
    for index, applicant in enumerate(sort_applications):
        if applicant.get("affirmative_action") is True:
            action_list.append(index)
        if len(action_list) == 3:
            break
    for index, number in enumerate(action_list):
        admitted.append(sort_applications.pop(number-index))
    for applicant in sort_applications:
        admitted.append(applicant)
        if len(admitted) is 30:
            break
    for index in range(6):
        wait_listed.append(sort_applications[index + 21])

    return admitted, wait_listed
