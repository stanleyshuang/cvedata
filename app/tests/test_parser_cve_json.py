# -*- coding: utf-8 -*-
#
# Author:   Stanley Huang
# Project:  crawler 1.0
# Date:     2021-07-10
#
import unittest
from pkg.util.parser_cve_json import is_cve_json_filename
from pkg.util.parser_cve_json import extract_cveid
from pkg.util.parser_cve_json import splitcveid

class IsCveJsonFilenameTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass
    
    def test_is_cve_json_filename_10(self):
        self.assertTrue(is_cve_json_filename('CVE-2021-28809'))
    
    def test_is_cve_json_filename_20(self):
        self.assertTrue(is_cve_json_filename('CVE-2021-3660'))
    
    def test_is_cve_json_filename_30(self):
        self.assertFalse(is_cve_json_filename('CVE-2021-3660.json'))
    
    def test_is_cve_json_filename_40(self):
        self.assertFalse(is_cve_json_filename('openpgp-encrypted-message'))
        

class ExtractCveidTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass
    
    def test_extract_cveid_10(self):
        self.assertTrue('CVE-2021-28491'==extract_cveid('CVE-2021-28491. - SQLite heap overflow'))
    
    def test_extract_cveid_20(self):
        self.assertTrue(None==extract_cveid('TYPO3 Form Designer backend module of the Form Framework is vulnerable to cross-site scripting'))
    
    def test_extract_cveid_30(self):
        self.assertTrue('CVE-2020-11575'==extract_cveid('Display and loop C codes, CVE-2020-11575, are vulnerable to heap based buffer overflow'))

        
class ExtractCveidTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass
    
    def test_splitcveid_10(self):
        self.assertTrue('2021', '28491'==splitcveid('CVE-2021-28491'))
    
    def test_splitcveid_20(self):
        self.assertTrue((None, None)==splitcveid('TYPO3 Form Designer backend module of the Form Framework is vulnerable to cross-site scripting'))
    
    def test_splitcveid_30(self):
        self.assertTrue('2020', '11575'==splitcveid('Display and loop C codes, CVE-2020-11575, are vulnerable to heap based buffer overflow'))

