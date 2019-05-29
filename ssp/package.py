from docx import Document

class SecurityPlan(object):

    def __init__(self, path):
        self.document = Document(path)