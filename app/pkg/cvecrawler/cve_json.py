#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Auther:   Stanley Huang
# Project:  crawler 1.0
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
