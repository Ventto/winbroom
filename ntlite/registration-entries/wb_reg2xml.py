# -*- coding: utf-8 -*-

import io
import os.path
import sys

def get_status(filepath):
        if not os.path.exists(filepath):
            print('Error: File not found.\n')
            sys.exit(1)
        return filepath

def parse_datatype(dataTypeStr):
    if dataTypeStr == '"':
        return 'REG_SZ'
    if dataTypeStr == 'dword':
        return 'REG_DWORD'
    if dataTypeStr == 'hex':
        return 'REG_BINARY'
    if dataTypeStr == 'hex(2)':
        return 'REG_EXPAND_SZ'
    if dataTypeStr == 'hex(7)':
        return 'REG_MULTI_SZ'
    return 'REG_SZ'

def parse_data(dataStr, regfile):
    if dataStr[0] == '"':
        return dataStr[1:len(dataStr)-2]
    if dataStr[-2] == '\\':
        hexdata = []

        hexdata.append(dataStr[0:-2].replace(",", ""))
        for line in regfile.readlines():
            if line[-2] == '\\':
                hexdata.append(line[1:-2])
            else:
                hexdata.append(line[1:-1])
                break
        return "".join(hexdata).replace(" ", "").replace(",", "")
    return dataStr[0:len(dataStr)-1]

def parse_value(line, regfile):
    valuedec = line.split('=')
    valuename = valuedec[0][1:len(valuedec[0])-1]
    dataInfo = valuedec[1].split(':');
    datatype = parse_datatype(dataInfo[0])

    if len(dataInfo) > 1:
        data = parse_data(dataInfo[1], regfile)
    else:
        data = parse_data(dataInfo[0], regfile)

    return "".join(['\t\t<value name="', valuename, '">\n',
                '\t\t\t<data>', data, '</data>\n', '\t\t\t<dataType>', datatype,
                '</dataType>\n', '\t\t</value>\n'])

# Convert REG file into XML string
def reg2xml(regfile):
    inSubkey = False
    delMode = False
    xmlstr = []

    xmlstr.append('<?xml version="1.0" encoding="utf-8"?>\n')
    xmlstr.append('<regEntries>\n')

    for line in regfile:
        if line[0] == '[':
            if inSubkey:
                xmlstr.append('\t</entry>\n')
            inSubkey = True
            delMode = False
            subkey_path = line[1:len(line)-2]
            if subkey_path[0] == '-':
                delMode = True
            if not delMode:
                xmlstr.append("".join(['\t<entry name="', subkey_path, '">\n']))
        else:
            if delMode:
                inSubkey = False
                continue
            if line[0] == '"':
                xmlstr.append(parse_value(line, regfile))

    if inSubkey:
        xmlstr.append('\t</entry>\n')
    xmlstr.append('</regEntries>\n')
    return "".join(xmlstr).expandtabs(tabsize=4)


def main(argv):
    if len(argv) != 2:
        print('Usage: wb_reg2xml.py file.REG \n')
        sys.exit(0)

    regpath_arg = argv[1]

    regfile = io.open(get_status(regpath_arg), 'r', encoding='utf-16-le')
    xmlstr = reg2xml(regfile)
    regfile.close()

    xmlfile = open('output.xml', 'w+')
    xmlfile.write(xmlstr)
    xmlfile.close()

if __name__ == "__main__":
    main(sys.argv)
