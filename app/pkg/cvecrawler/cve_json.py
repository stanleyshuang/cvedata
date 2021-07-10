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
