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

    def __repr__(self):
        return self.number

    def __iter__(self):
        return iter(self.parts)

    def get_parts(self):
        self.parts = []
        for row in self.implementation_table.rows:
            if "Part" in row.cells[0].text and len(row.cells[0].text) < 8:
                self.parts.append(row.cells[0].text.replace('Part ', '').strip())
            elif len(self.parts) < 1 and len(self.implementation_table.rows) < 3:
                self.parts.append(None)

    def part(self, part_id):
        if part_id == None:
            return self.implementation_table.cell(1,0)
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
                return self.implementation_table.cell(self.LETTERS[part_id], 1)
        else:
            raise ValueError('Control does not have part ' + part_id)