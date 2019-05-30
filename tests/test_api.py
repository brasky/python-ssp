"""
Test suite for ssp.api module.
"""
import os
import sys

import pytest
import docx

import ssp
from ssp.api import SSP

TEST_DIR = os.path.dirname(os.path.abspath(__file__))

class TestAPI(object):

    def test_that_word_doc_opens(self):
        path = TEST_DIR + '/test_files/test.docx'
        securityplan = SSP(path)
        assert isinstance(securityplan, ssp.securityplan.SecurityPlan)
