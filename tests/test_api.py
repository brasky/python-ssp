"""
Test suite for ssp.api module.
"""
import os
import sys

import pytest
import docx

from ssp.api import SSP

TEST_DIR = os.path.dirname(os.path.abspath(__file__))

def test():
    path = TEST_DIR + '\\test_files\\test.docx'
    securityplan = SSP(path)
    assert isinstance(securityplan.document, docx.document.Document)
