from string import ascii_lowercase
import re

class Control(object):
    """
    Control object, created by passing CIS table and Implementation table for 1 control. 
    """
    LETTERS = {letter: index for index, letter in enumerate(ascii_lowercase, start=1)} 

    def __init__(self, cis_table, implementation_table):
        self.cis_table = cis_table
        self.implementation_table = implementation_table
        self.number = cis_table.cell(0,0).text
        self.get_parts()
        self.get_responsible_role()
        self.parameters = []
        rows = len(self.cis_table.rows)
        for row in range(2, rows-2):
            self.add_to_parameters(self.cis_table.rows[row].cells[0])
        self.get_implementation_status(self.cis_table.rows[rows-2].cells[0])
        self.get_control_origination(self.cis_table.rows[rows-1].cells[0])

    def __repr__(self):
        return self.number

    def __iter__(self):
        return iter(self.parts)

    def get_parts(self):
        self.parts = []
        for row in self.implementation_table.rows:
            if "Part" in row.cells[0].text and len(row.cells[0].text) < 8:
                self.parts.append(row.cells[0].text.replace('Part ', '').strip())
            elif 'Req.' in row.cells[0].text and len(row.cells[0].text) < 8:
                self.parts.append(row.cells[0].text.replace('Req. ', '').strip())

        if len(self.parts) < 1 and len(self.implementation_table.rows) < 3:
            self.parts.append(None)

    def part(self, part_id):
        """
        Takes string part_id and returns corresponding implementation cell object.
        """
        if part_id == None:
            try:
                return self.implementation_table.cell(1,0)
            except IndexError:
                raise IndexError('Control table %s does not have enough rows to contain a control response.' % (self.number))

        if part_id in self.parts:
            split_alpha_part = re.compile(r'\w\d')
            if split_alpha_part.match(part_id):
                try:
                    letter = part_id[0]
                    row_difference = int(part_id[1]) - 1
                    return self.implementation_table.cell(self.LETTERS[letter]+row_difference, 1)
                except:
                    ValueError('Control does not have part ' + part_id)
            else:
                try:
                    return self.implementation_table.cell(self.LETTERS[part_id], 1)
                except KeyError:
                    return self.implementation_table.cell(int(part_id), 1)
        else:
            raise ValueError('Control does not have part ' + part_id)

    def get_responsible_role(self):
        """
        Adds responsible role text to control object.
        """
        self.responsible_role = self.cis_table.cell(1,0).text.replace('Responsible Role:', '').strip()

    def add_to_parameters(self, cell):
        """
        Appends parameter cell text to control object parameter list.
        """
        self.parameters.append(cell.text.strip())
            
    def get_implementation_status(self, cell):
        """
        Appends implementation status checkbox data to control object implementation status list.
        """
        self.implementation_status = []
        for paragraph in cell.paragraphs:
            p = paragraph._element
            if 'w14:checked w14:val="1"' in p.xml:
                xpath_elements = p.xpath('.//w:t')
                implementation_status = xpath_elements[len(xpath_elements)-1].text.strip()
                if 'Partially' in implementation_status:
                    self.implementation_status.append('Partially Implemented')
                elif 'Implemented' in implementation_status:
                    self.implementation_status.append('Implemented')
                elif 'Planned' in implementation_status:
                    self.implementation_status.append('Planned')
                elif 'Alternative' in implementation_status:
                    self.implementation_status.append('Alternative Implementation')
                elif 'Not' in implementation_status:
                    self.implementation_status.append('Not Applicable')
            elif '<w:checked/>\n' in p.xml or '<w:default w:val="1"/>' in p.xml:
                #old style of checkboxes...
                implementation_status = paragraph.text.strip()
                if 'Partially' in implementation_status:
                    self.implementation_status.append('Partially Implemented')
                elif 'Implemented' in implementation_status:
                    self.implementation_status.append('Implemented')
                elif 'Planned' in implementation_status:
                    self.implementation_status.append('Planned')
                elif 'Alternative' in implementation_status:
                    self.implementation_status.append('Alternative Implementation')
                elif 'Not' in implementation_status:
                    self.implementation_status.append('Not Applicable')

    def get_control_origination(self, cell):
        """
        Appends control origination checkbox data to control object control origination list.
        """
        self.control_origination = []
        for paragraph in cell.paragraphs:
            p = paragraph._element
            if 'w14:checked w14:val="1"' in p.xml:
                xpath_elements = p.xpath('.//w:t')
                control_origination = xpath_elements[len(xpath_elements)-1].text.strip()
                if not control_origination:
                    control_origination = xpath_elements[len(xpath_elements)-2].text.strip() #TODO: this is really ugly, but had to be done because inherited checkboxes werent being captured.
                if "Service Provider Corporate" in control_origination:
                    self.control_origination.append("Service Provider Corporate")
                elif "Service Provider System Specific" in control_origination:
                    self.control_origination.append("Service Provider System Specific")
                elif "Hybrid" in control_origination:
                    self.control_origination.append("Service Provider Hybrid")
                elif "Configured" in control_origination:
                    self.control_origination.append("Configured by Customer")
                elif "Provided" in control_origination:
                    self.control_origination.append("Provided by Customer")
                elif "Shared" in control_origination:
                    self.control_origination.append("Shared")
                elif "Inherited" in control_origination:
                    self.control_origination.append("Inherited")
                elif "Not" in control_origination:
                    self.control_origination.append("Not Applicable")
            elif '<w:checked/>\n' in p.xml or '<w:default w:val="1"/>' in p.xml:
                control_origination = paragraph.text.strip()
                if "Service Provider Corporate" in control_origination:
                    self.control_origination.append("Service Provider Corporate")
                elif "Service Provider System Specific" in control_origination:
                    self.control_origination.append("Service Provider System Specific")
                elif "Hybrid" in control_origination:
                    self.control_origination.append("Service Provider Hybrid")
                elif "Configured" in control_origination:
                    self.control_origination.append("Configured by Customer")
                elif "Provided" in control_origination:
                    self.control_origination.append("Provided by Customer")
                elif "Shared" in control_origination:
                    self.control_origination.append("Shared")
                elif "Inherited" in control_origination:
                    self.control_origination.append("Inherited")
                elif "Not" in control_origination:
                    self.control_origination.append("Not Applicable")
