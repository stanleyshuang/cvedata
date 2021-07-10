#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Auther:   Stanley Huang
# Project:  crawler 1.0
# Date:     2021-07-10
#
import os
from . import i_crawler

class cveproject(i_crawler):
    def __init__(self):
        super(cveproject, self).__init__()
        self.b_run_loaddb = False
        self.apphome = ''

    def set_apphome(self, apphome):
        self.apphome = apphome

    def loaddb(self):
        if self.b_run_loaddb:
            return

        self.b_run_loaddb = True
        ### Get shell commend and run
        if not os.path.isdir(self.apphome + '/cvelist'):
            os.system('cd {apphome}'.format(apphome=self.apphome))
            os.system('git clone https://github.com/stanleyshuang/cvelist.git')
        shellfolder = self.apphome + '/shell'
        os.system(shellfolder + '/sync.sh')