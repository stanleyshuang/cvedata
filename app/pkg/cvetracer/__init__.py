#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Auther:   Stanley Huang
# Project:  tracer 1.0
# Date:     2021-07-10
#
import abc

class i_tracer():
    __metaclass__ = abc.ABCMeta
    
    def __init__(self):
        pass

    @abc.abstractmethod
    def set(self, *args, **kwargs):
        print('set', args, kwargs)

    @abc.abstractmethod
    def dump(self):
        print('dump')

    @abc.abstractmethod
    def run(self):
        print('run')
        
    