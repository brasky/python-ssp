[![Build Status](https://travis-ci.org/brasky/python-ssp.svg?branch=master)](https://travis-ci.org/brasky/python-ssp)

# Table of Contents
* [Overview](#Overview)
* [Installation](#Installation)
* [Usage](#Usage)
    * [Opening an SSP](#Opening-an-SSP)
    * [Viewing controls](#Viewing-controls)
    * [Control attributes](#control-attributes)


# Overview

*python-ssp* is a Python library for interfacing with FedRAMP system security plan templates. It uses *[python-docx](https://github.com/python-openxml/python-docx)* as a base so controls can be accessed using the SSP api or using the underlying docx table object which allows both simplicity when you want it and feature richness depending on the use case.

*python-ssp* is currently in an early development phase and was inspired to simplify import/export code in another project of mine, *[securityplanmanager](https://github.com/brasky/securityplanmanager)*.

# Installation 

Installation can be done either by cloning this repository:

```
git clone https://github.com/brasky/python-ssp.git
cd python-ssp
pip install -e .
```

or via pip directly:
```
pip install python-ssp
```

## Dependencies
- python-docx
    - Python 3.3+
    - lxml >= 2.3.2

# Usage

## Opening an SSP

First thing to do is open an SSP. Currently the only version supported is the newest template as of 7/4/2019 released 08/28/2018 on fedramp.gov/templates.

```python
from ssp import SSP

security_plan = SSP('path\to\securityplan.docx')
```

If you get an error here, it could be because your document is not a supported template, or because of a Word object called "Content Controls" which are in the template around every table. To remove them, save the document as a .doc, it will tell you that it will remove content controls, then save it back to a .docx.

## Viewing controls

Once your SSP is open, you probably want to look at information about your implementations. You can do this in a variety of ways:

### Get a list of all the controls

An SSP object has a control_list attribute which has a list of all the controls that were identified on import. The `__iter__`  method is defined to return the control_list. You can loop through every control like so
```python
for control in security_plan:
...
```

### Get one specific control

To get a specific control you can use the `control` method which will return the corresponding control object
```python
security_plan.control('AC-1')
```

Control objects are defined as a pair of tables (the CIS table and the implementation table), so they are the base control that is listed in the first cell of the CIS table. That's why it's passed `'AC-1'` as the control and not `'AC-1(a)'`.

### Control parts

After getting the control object you want, you can either get the part you want or get the list of parts the control has. Parts are equivalent to rows in the implementations table. 

The part list is defined in the `parts` control attribute. For example, `security_plan.control('AC-2').parts` should return a list of parts 'a' through 'k'. The `__iter__` for control objects will iterate through parts, so you can do `for part in control` to loop through all the parts.

The `part()` method allows you to specify the part you want with `security_plan.control('AC-2').part('a')` and returns a docx cell object. To get the text you just add `.text`, so `security_plan.control('AC-2').part('a').text` will give you the implementation for AC-2(a).

If a control has no parts and just 1 implementation row, `.parts` will return `[None]` and `.parts(None)` will return the cell object for that implementation. For example:

```python
security_plan.control('AC-2(3)').parts(None).text
```

 This is an example of the alpha development phase in action and will be changed soon to something more readable.

## Control Attributes

Other control details are accessed through the following attributes:
### Control Number
`control_object.number` will return the control number as it's written in the first cell of the CIS table, so if you are looping through controls and you `print(control_object.number)` it will print "AC-2".

### Responsible Role
`security_plan.control('AC-2').responsible_role` will return everything to the right of the colon in the responsible role field as a string.

### Control Origination
`security_plan.control('AC-2').control_origination` will return a list of all the boxes checked in the control origination section.

### Parameters
`security_plan.control('AC-2').parameters` will return a list of all the parameter fields.

### Implementation Status
`security_plan.control('AC-2').implementation_status` will return a list of all the boxes checked in the implementation status section.