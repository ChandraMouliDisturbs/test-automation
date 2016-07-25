"""Concept Coach v2, Epic 11 - Improve Question Management."""

import inspect
import json
import os
import pytest
import unittest

from pastasauce import PastaSauce, PastaDecorator
from random import randint  # NOQA
from selenium.webdriver.common.by import By  # NOQA
from selenium.webdriver.support import expected_conditions as expect  # NOQA
from staxing.assignment import Assignment  # NOQA

# select user types: Admin, ContentQA, Teacher, and/or Student
from staxing.helper import Teacher, Student  # NOQA

basic_test_env = json.dumps([{
    'platform': 'OS X 10.11',
    'browserName': 'chrome',
    'version': '50.0',
    'screenResolution': "1024x768",
}])
BROWSERS = json.loads(os.getenv('BROWSERS', basic_test_env))
TESTS = os.getenv(
    'CASELIST',
    str([14851, 14852, 14853, 14854, 14855, 14856, 14858, 14859])  # NOQA
)


@PastaDecorator.on_platforms(BROWSERS)
class TestIImproveQuestionManagement(unittest.TestCase):
    """CC2.11 - Improve Question Management."""

    def setUp(self):
        """Pretest settings."""
        self.ps = PastaSauce()
        self.desired_capabilities['name'] = self.id()
        self.Teacher = Teacher(
            use_env_vars=True,
            pasta_user=self.ps,
            capabilities=self.desired_capabilities
        )

    def tearDown(self):
        """Test destructor."""
        self.ps.update_job(job_id=str(self.teacher.driver.session_id),
                           **self.ps.test_updates)
        try:
            self.teacher.delete()
        except:
            pass

    # 14851 - 001 - Teacher | Review all questions
    @pytest.mark.skipif(str(14851) not in TESTS, reason='Excluded')  # NOQA
    def test_teacher_review_all_questions_14851(self):
        """Review all questions.

        Steps:

        Go to https://tutor-qa.openstax.org/
        Click on the 'Login' button
        Enter the teacher user account in the username and password text boxes
        Click on the 'Sign in' button
        If the user has more than one course, click on a CC course name

        Click "Question Library" from the user menu
        Select a section or chapter
        Click "Show Questions"



        Expected Result:

        The user is presented with all the questions for the section or chapter

        """
        self.ps.test_updates['name'] = 'cc2.11.001' \
            + inspect.currentframe().f_code.co_name[4:]
        self.ps.test_updates['tags'] = [
            'cc2',
            'cc2.11',
            'cc2.11.001',
            '14851'
        ]
        self.ps.test_updates['passed'] = False

        # Test steps and verification assertions

        self.ps.test_updates['passed'] = True

    # 14852 - 002 - Teacher | Exclude certain questions
    @pytest.mark.skipif(str(14852) not in TESTS, reason='Excluded')  # NOQA
    def test_teacher_exclude_certain_questions_14852(self):
        """Exclude certain quesitons.

        Steps:

        If the user has more than one course, click on a CC course name

        Click "Question Library" from the user menu
        Select a section or chapter
        Click "Show Questions"
        Hover over the desired question and click "Exclude question"


        Expected Result:

        Question is grayed out

        """
        self.ps.test_updates['name'] = 'cc2.11.002' \
            + inspect.currentframe().f_code.co_name[4:]
        self.ps.test_updates['tags'] = [
            'cc2',
            'cc2.11',
            'cc2.11.002',
            '14852'
        ]
        self.ps.test_updates['passed'] = False

        # Test steps and verification assertions

        self.ps.test_updates['passed'] = True

    # 14855 - 003 - Teacher | Pin tabs on top of screen when scrolled
    @pytest.mark.skipif(str(14855) not in TESTS, reason='Excluded')  # NOQA
    def test_teacher_pin_tabs_on_top_of_screen_when_scrolled_14855(self):
        """Pin tabs on top of screen when scrolled.

        Steps:

        If the user has more than one course, click on a CC course name

        Click "Question Library" from the user menu
        Select a section or chapter
        Click "Show Questions"
        Scroll down


        Expected Result:

        Tabs are pinned to top of the screen when scrolled

        """
        self.ps.test_updates['name'] = 'cc2.11.003' \
            + inspect.currentframe().f_code.co_name[4:]
        self.ps.test_updates['tags'] = [
            'cc2',
            'cc2.11',
            'cc2.11.003',
            '14855'
        ]
        self.ps.test_updates['passed'] = False

        # Test steps and verification assertions

        self.ps.test_updates['passed'] = True

    # 14856 - 004 - Teacher | Make section links jumpable
    @pytest.mark.skipif(str(14856) not in TESTS, reason='Excluded')  # NOQA
    def test_teacher_make_section_links_jumpable_14856(self):
        """Make section links jumpable.

        Steps:

        If the user has more than one course, click on a CC course name

        Click "Question Library" from the user menu
        Select a section or chapter
        Click "Show Questions"
        Click on the section links at the top of the screen


        Expected Result:

        The screen scrolls to the selected questions

        """
        self.ps.test_updates['name'] = 'cc2.11.004' \
            + inspect.currentframe().f_code.co_name[4:]
        self.ps.test_updates['tags'] = [
            'cc2',
            'cc2.11',
            'cc2.11.004',
            '14856'
        ]
        self.ps.test_updates['passed'] = False

        # Test steps and verification assertions

        self.ps.test_updates['passed'] = True

    # 14858 - 005 - Teacher | Report errata about assessments in Concept Coach
    @pytest.mark.skipif(str(14858) not in TESTS, reason='Excluded')  # NOQA
    def test_teacher_report_errata_about_assessments_in_cc_14858(self):
        """Report errata about assessments in Concept Coach.

        Steps:

        If the user has more than one course, click on a CC course name

        Click "Question Library" from the user menu
        Select a section or chapter
        Click "Show Questions"
        Hover over the desired question and click "Question details"
        Click "Report an error"


        Expected Result:

        A new tab with the assessment errata form appears, with the assessment
        ID already filled in

        """
        self.ps.test_updates['name'] = 'cc2.11.005' \
            + inspect.currentframe().f_code.co_name[4:]
        self.ps.test_updates['tags'] = [
            'cc2',
            'cc2.11',
            'cc2.11.005',
            '14858'
        ]
        self.ps.test_updates['passed'] = False

        # Test steps and verification assertions

        self.ps.test_updates['passed'] = True

    # 14859 - 006 - Student | Report errata about assessments in Concept Coach
    @pytest.mark.skipif(str(14858) not in TESTS, reason='Excluded')  # NOQA
    def test_student_report_errata_about_assessments_in_cc_14859(self):
        """Report errata about assessments in Concept Coach.

        Steps:

        Click on a CC course, if there are more than one

        Click on a non-introductory section
        Click "Jump to Concept Coach"
        Click "Launch Concept Coach"
        Click "Report an error" on an assessment

        Expected Result:

        A new tab with the assessment errata form appears, with the assessment
        ID already filled in

        """
        self.ps.test_updates['name'] = 'cc2.11.006' \
            + inspect.currentframe().f_code.co_name[4:]
        self.ps.test_updates['tags'] = [
            'cc2',
            'cc2.11',
            'cc2.11.006',
            '14859'
        ]
        self.ps.test_updates['passed'] = False

        # Test steps and verification assertions

        self.ps.test_updates['passed'] = True