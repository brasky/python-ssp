"""
Test suite for ssp.securityplan module.
"""
import os
import sys

import pytest
import docx

from ssp.securityplan import SecurityPlan

TEST_DIR = os.path.dirname(os.path.abspath(__file__))

class TestSecurityPlan(object):
    
    def test_that_word_doc_opens(self):
        """
        Make sure basic word docs open, basically testing docx is working.
        """
        path = TEST_DIR + '/test_files/test.docx'
        securityplan = SecurityPlan(path)
        assert isinstance(securityplan.document, docx.document.Document)
    
    def test_get_version_returns_correct_version(self):
        """
        Test that the proper versions are obtained from template
        """
        version = '08282018'
        path = TEST_DIR + '/test_files/blank_templates/' + version + '/'
        file_name = 'FedRAMP-SSP-High-Baseline-Template.docx'

        securityplan = SecurityPlan(path + file_name)
        assert securityplan.version == version

    def test_control(self):
        control = 'AC-1'
        version = '08282018'
        path = TEST_DIR + '/test_files/blank_templates/' + version + '/'
        file_name = 'FedRAMP-SSP-High-Baseline-Template.docx'
    
        securityplan = SecurityPlan(path + file_name)

        control_object = securityplan.control(control)
        assert control_object.number == control