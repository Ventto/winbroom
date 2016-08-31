#!/usr/bin/env python3

import io
import sys

# Get the value's datatype
def parse_datatype(dataTypeStr):
    if dataTypeStr[0] == '"':
        return 'REG_SZ'
    if dataTypeStr[0] == 'dword':
        return 'REG_DWORD'
    if dataTypeStr[0] == 'hex':
        return 'REG_BINARY'
    if dataTypeStr[0] == 'hex(2)':
        return 'REG_EXPAND_SZ'
    if dataTypeStr[0] == 'hex(7)':
        return 'REG_MULTI_SZ'
    return 'REG_SZ'

# Get the value's data
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

regfile_arg = sys.argv[1]
regfile = io.open(regfile_arg, 'r', encoding='utf-16-le')

inSubkey = False
extendedData = 1
delMode = False

for line in regfile:
    # Read the subkey
    if line[0] == '[':
        delMode = False
        subkey_path = line[1:len(line)-2]
        if subkey_path[0] == '-':
            delMode = True
        if not delMode:
            print ("".join(['[SUBKEY]\n', subkey_path, '\n']))
    else:
        if delMode:
            continue
        # Read the value
        if line[0] == '"':
            extendedData = 1
            valuedec = line.split('=')
            valuename = valuedec[0][1:len(valuedec[0])-1]
            dataInfo = valuedec[1].split(':');
            datatype = parse_datatype(dataInfo[0])
            if len(dataInfo) > 1:
                data = parse_data(dataInfo[1], regfile)
            else:
                data = parse_data(dataInfo[0], regfile)
            print ("".join(['value:', valuename, '\ntype:',
                datatype, '\ndata:', '{', data, '}\n']))

regfile.close()
