#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Auther:   Stanley Huang
# Project:  crawler 1.0
# Date:     2021-07-10
#
import os, sys

from pkg.cvecrawler.cve_json import is_cve_json_filename
from pkg.util.util_file import create_folder, get_name_list_of_files

def usage():
    print('USAGE:    python main.py cmd')
    print('--')
    print('cmd:      --test for unit test')
    quit()
    
if len(sys.argv) == 1:
    usage()
    quit()

### get argv[1] as input
for idx in range(1, len(sys.argv)):
    if sys.argv[idx] in ['--test']:
        cmd = sys.argv[idx][2:]
    elif sys.argv[idx] in ['test']:
        cmd = sys.argv[idx]
    else:
        pass

### the main program
# Get environment variables

### Create downloads folder
apphome = os.environ.get('apphome')
downloads = apphome + '/downloads'
create_folder(downloads)

### Enumerate inputs folder
inputs = apphome + '/inputs'
filelist = get_name_list_of_files(inputs)
for file in filelist:
    filename, file_extension = os.path.splitext(file)
    print('{filename} {file_extension}'.format(filename=filename, file_extension=file_extension))

if cmd=='test':
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
else: 
    usage()
