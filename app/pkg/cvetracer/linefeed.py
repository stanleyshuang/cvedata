#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Auther:   Stanley Huang
# Project:  tracer 1.0
# Date:     2021-07-10
#
import os
from pkg.util.util_text_file import get_lines
from pkg.util.parser_cve_json import extract_cveid

from . import i_tracer

class linefeed(i_tracer):
    def __init__(self):
        super(linefeed, self).__init__()
        self.input_file = ''
        self.crawler = None

    def set_input(self, input_file):
        self.input_file = input_file

    def set_crawler(self, crawler):
        self.crawler = crawler

    def run(self):
        lines = get_lines(self.input_file)
        for line in lines:
            cveid = extract_cveid(line)
            if cveid:
                self.crawler.read(cveid)

                