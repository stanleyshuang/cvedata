#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Auther:   Stanley Huang
# Project:  parser_cve_json 1.0
# Date:     2021-07-10
#
import datetime, re

def is_cve_json_filename(filename):
    # CVE regular expression
    cve_pattern = r'^CVE-\d{4}-\d{4,7}$'
    is_cve = re.match(cve_pattern, filename)
    return is_cve

def extract_cveid(content):
    '''
    example: CVE-2021-28491. - SQLite heap overflow
    return: CVE-2021-28491
    '''
    m = re.search(r"(CVE-\d{4}-\d{4,7})", content)
    if m:
        return m.group(0)
    return None

def splitcveid(cveid):
    '''
    example: CVE-2021-28491
    return: CVE-2021-28491
    '''
    m = re.search(r"(CVE-\d{4}-\d{4,7})", cveid)
    if m:
        cveid = m.group(0)
        idx = cveid.find('-', 4)
        year = cveid[4:idx]
        caseid = cveid[idx+1:]
        return year, caseid
    return None, None
