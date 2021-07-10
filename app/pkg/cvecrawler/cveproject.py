#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Auther:   Stanley Huang
# Project:  crawler 1.0
# Date:     2021-07-10
#
import os
from pkg.util.util_text_file import open_json
from pkg.util.parser_cve_json import splitcveid

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

    def read(self, cveid):
        year, caseid = splitcveid(cveid)
        if year and caseid:
            the_path = self.apphome + '/cvelist/' + year + '/' + caseid[0:-3] + 'xxx'
            the_file = cveid + '.json'
            cvejson = '{the_path}/{the_file}'.format(the_path=the_path, the_file=the_file)
            if os.path.exists(cvejson):
                cvedata = open_json(cvejson)
                if cvedata:
                    if 'impact' in cvedata:
                        if 'cvss' in cvedata['impact']:
                            if 'baseScore' in cvedata['impact']['cvss']:
                                score = cvedata['impact']['cvss']['baseScore']
                                print('{cveid}, {score}'.format(cveid=cveid, score=score))
                            else:
                                print('{cveid} no baseScore'.format(cveid=cveid))
                        else:
                            print('{cveid} no cvss'.format(cveid=cveid))
                    else:
                        print('{cveid} no impact'.format(cveid=cveid))
                else:
                    print('{cvejson} is not cve_json'.format(cvejson=cvejson))
            else:
                print('{cvejson} does not exist'.format(cvejson=cvejson))