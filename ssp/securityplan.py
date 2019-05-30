from docx import Document

class SecurityPlan(object):
    """
    Not intended to be constructed directly. Use ssp.api.SSP() to open an SSP.
    """

    tables = []
    table_name_to_table_index = {}

    def __init__(self, path):
        self.document = Document(path)
        self.tables = self.document.tables
        self.version = self.get_version()
        self.child_ssp = None
        if self.version == '08282018':
            self.child_ssp = SecurityPlan_08282018(self)
        else:
            raise ValueError('This template version is not compatible.')
        self.child_ssp.create_table_index()
        self.table_name_to_table_index = self.child_ssp.table_name_to_table_index

    def get_version(self):
        """
        Needs to take a Document file and return either a version number or raise an error if not an ssp.
        """
        # For some reason docx doesn't see anything before the table of contents in the list of tables or paragraphs, will need to parse document._element.xml
        # template_revision_table_index = self.table_name_to_table_index['Date']
        # template_revision_table = self.tables[template_revision_table_index]
        # try:
        #     date = template_revision_table.cell(7, 0).text
        #     if date == '8/28/2018':
        #         return '08282018'
        #     else:
        #         raise ValueError
        # except:
        #     raise ValueError('Error getting version, has the template revision history been altered? Possibly unsupported template')
        return '08282018'

class SecurityPlan_08282018(SecurityPlan):
    """
    Child class for the SSP version published 08/28/2018. 
    Takes an SSP object and returns a child SSP object specific to this template.
    """
    
    def __init__(self, ssp):
        self.document = ssp.document
        self.tables = ssp.document.tables
        self.create_table_index()

    def create_table_index(self):
        """
        Fills the table index dictionary.
        table_name (i.e. Cell(0,0).text) = position in table array
        """
        for index, table in enumerate(self.tables):
            try:
                self.table_name_to_table_index[table.cell(0,0).text] = index
            except:
                # Need to incorporate logging
                self.table_name_to_table_index['blank'] = index 
