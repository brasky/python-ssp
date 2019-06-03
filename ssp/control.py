

class Control(object):
    """
    Control object, created by passing CIS table and Implementation table for 1 control. 
    """
    number = ''

    def __init__(self, cis_table, implementation_table):
        self.cis_table = cis_table
        self.implementation_table = implementation_table
        self.number = cis_table.cell(0,0).text

    def __repr__(self):
        return self.number