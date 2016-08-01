"""Concept Coach v1, Epic 15 - OpenStax Metrics."""

import inspect
import json
import os
import pytest
import unittest

from pastasauce import PastaSauce, PastaDecorator
# from random import randint
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as expect
# from staxing.assignment import Assignment

# select user types: Admin, ContentQA, Teacher, and/or Student
from staxing.helper import Teacher

basic_test_env = json.dumps([{
    'platform': 'OS X 10.11',
    'browserName': 'chrome',
    'version': '50.0',
    'screenResolution': "1024x768",
}])
BROWSERS = json.loads(os.getenv('BROWSERS', basic_test_env))
TESTS = os.getenv(
    'CASELIST',
    str([7608])
)


@PastaDecorator.on_platforms(BROWSERS)
class TestOpenStaxMetrics(unittest.TestCase):
    """CC1.15 - OpenStax Metrics."""

    def setUp(self):
        """Pretest settings."""
        self.ps = PastaSauce()
        self.desired_capabilities['name'] = self.id()
        self.teacher = Teacher(
            use_env_vars=True,
            pasta_user=self.ps,
            capabilities=self.desired_capabilities
        )

    def tearDown(self):
        """Test destructor."""
        self.ps.update_job(
            job_id=str(self.teacher.driver.session_id),
            **self.ps.test_updates
        )
        try:
            self.teacher.delete()
        except:
            pass

    # Case C7608 - 001 - Admin | View a report of enrolled students by course
    @pytest.mark.skipif(str(7608) not in TESTS, reason='Excluded')
    def test_admin_view_a_report_of_enrolled_students_by_course_7608(self):
        """View a report of enrolled students by course.

        Steps:
        Go to https://tutor-qa.openstax.org/
        Click on the 'Login' button
        Enter the admin user account in the username and password text boxes
        Click on the 'Sign in' button
        Click on the 'Admin' button from the user menu
        Open the drop down menu by clicking 'Course Organization'
        Click the 'Courses' option
        Click the 'List Students' button for the chosen course

        Expected Result:
        List of students for chosen course is displayed
        """
        self.ps.test_updates['name'] = 'cc1.15.001' \
            + inspect.currentframe().f_code.co_name[4:]
        self.ps.test_updates['tags'] = [
            'cc1',
            'cc1.15',
            'cc1.15.001',
            '7608'
        ]
        self.ps.test_updates['passed'] = False

        # Test steps and verification assertions
        raise NotImplementedError(inspect.currentframe().f_code.co_name)

        self.ps.test_updates['passed'] = True
