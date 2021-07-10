#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Auther:   Stanley Huang
# Project:  crawler 1.0
# Date:     2021-07-10
#
import os, sys

from pkg.cvecrawler.cveproject import cveproject
from pkg.cvetracer.linefeed import linefeed
from pkg.util.util_file import create_folder, get_name_list_of_files

def usage():
    print('USAGE:    python main.py cmd')
    print('--')
    print('cmd:      --test for unit test')
    print('          --crawler for default')
    quit()

def env_init():
    apphome = os.environ.get('apphome')

    ### Create downloads
    downloads = apphome + '/downloads'
    create_folder(downloads)

###################################################
### main program begin
if len(sys.argv) == 1:
    usage()
    quit()

# get argv[1] as input
cmd = 'crawler'
for idx in range(1, len(sys.argv)):
    if sys.argv[idx] in ['--test']:
        cmd = sys.argv[idx][2:]
    elif sys.argv[idx] in ['test']:
        cmd = sys.argv[idx]
    else:
        pass

# parse command and execute
if cmd=='test':
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
else:
    apphome = os.environ.get('apphome')

    env_init()
    cveproject = cveproject()
    cveproject.set_apphome(apphome)
    cveproject.loaddb()

    ### Enumerate inputs
    inputs = apphome + '/inputs'
    filelist = get_name_list_of_files(inputs)

    for file in filelist:
        linefeed = linefeed()
        linefeed.set_input(inputs + '/' + file)
        linefeed.set_crawler(cveproject)
        linefeed.run()

