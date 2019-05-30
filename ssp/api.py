import os

from ssp.securityplan import SecurityPlan

import docx

def SSP(ssp=None):
    """
    Return an SSP object loaded from a .docx file.
    """

    if ssp is None:
        raise ValueError("Path to SSP required.")
    return SecurityPlan(ssp)