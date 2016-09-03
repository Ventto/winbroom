# -*- coding: utf-8 -*-

import sys
import xml.etree.ElementTree as ET

xmlfile_arg = sys.argv[1]

tree = ET.parse(xmlfile_arg)
root = tree.getroot()

f = open('wb_activesetup.bat', 'w')

for entry in root.findall('entry'):
    keypath = entry.get('name')
    keyname = keypath.split('\\')[-1]

    for value in entry.findall('value'):
        valuename = value.get('name')
        data = value.find('data').text
        datatype = value.find('dataType').text
        cmd = ''.join(['reg add ',
                '"HKLM\SOFTWARE\Microsoft\Active Setup\Installed Components\\',
                keyname, '-', valuename,
                '" ^\n\t/v "Version" ^\n\t/d "1" /f\n reg add ',
                '"HKLM\SOFTWARE\Microsoft\Active Setup\Installed Components\\',
                keyname, '-', valuename,
                '" ^\n\t/v "StubPath" ^\n\t/d "reg add ',
                keypath, ' /v "', valuename, '" /d "', data, '" /t ', datatype,
                " /f\" ^\n\t/f\n"])
        f.write(cmd)
    f.write("\n\n")
