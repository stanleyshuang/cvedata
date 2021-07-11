#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Auther:   Stanley Huang
# Project:  crawler 1.0
# Date:     2021-07-11
#
import os
import requests
import time
from bs4 import BeautifulSoup
from pkg.util.util_text_file import open_json
from pkg.util.parser_cve_json import splitcveid

from . import i_crawler

class nvdweb(i_crawler):
    def __init__(self):
        super(nvdweb, self).__init__()
        self.response = None

    def loaddb(self):
        pass

    def read(self, cveid):
        time.sleep(3)
        self.response = requests.get('https://nvd.nist.gov/vuln/detail/' + cveid)
        soup = BeautifulSoup(self.response.text, 'html.parser')
        try:
            value = soup.find('input', {'id': 'cnaV3MetricHidden'}).get('value')
            bs = BeautifulSoup(value)
            span = bs.find('span', {'id': 'nistV3Metric'})
            # span
            p = span.find('p', {'data-testid': 'vuln-cvssv3-score-container'})
            # span p
            score = p.find('span', {'data-testid': 'vuln-cvssv3-base-score'})
            # span p span
            print('[{cveid}] score: {score}'.format(cveid=cveid, score=score.text))
        except Exception as e:
            print('[{cveid}] unhandled exception: {ex}'.format(cveid=cveid, ex=str(e)))

