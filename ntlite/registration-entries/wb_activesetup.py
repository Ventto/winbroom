# -*- coding: utf-8 -*-

from xml.etree.ElementTree import ParseError
import os
import sys.exit
import xml.etree.ElementTree as ET

def get_status(filepath):
        if not os.path.exists(filepath):
            print('Error: File not found.\n')
            sys.exit(1)
        return filepath

def main(argv):
    if len(argv) != 2:
        print('Usage: wb_activesetup.py file.XML \n', file=sys.stderr)
        sys.exit(0)

    try:
        tree = ET.parse(get_status(argv[1]))
    except ParseError:
        tree = None

    if tree == None:
        print('Error: Bad XML syntax.\n', file=sys.stderr)
        sys.exit(1)

    root = tree.getroot()

    batfile = open('activesetup.bat', 'w')

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
            batfile.write(cmd)

        batfile.write("\n\n")

if __name__ == "__main__":
    main(sys.argv)
