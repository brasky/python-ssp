from docx import Document

from ssp.control import Control


class TestControl(object):

    def test_control_creation(self):
        #need to make a better test ssp for this, just a quick test...
        ssp = Document(r'tests\test_files\blank_templates\08282018\FedRAMP-SSP-High-Baseline-Template.docx')
        cis_table = ''
        implementation_table = ''
        next_table_is_implementation_details = False
        for table in ssp.tables:
            try:
                if table.cell(0,0).text == 'AC-1':
                    next_table_is_implementation_details = True
                    cis_table = table
                elif next_table_is_implementation_details:
                    implementation_table = table
                    test_control = Control(cis_table, implementation_table)
                    break
            except IndexError:
                pass

        assert test_control.number == 'AC-1'
        assert test_control.cis_table == cis_table
        assert test_control.implementation_table == implementation_table


