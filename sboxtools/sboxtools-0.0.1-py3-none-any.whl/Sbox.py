# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 09:41:15 2022


@author: Donggeun Kwon (donggeun.kwon at gmail.com)

Cryptographic Algorithm Lab.
Institute of Cyber Security & Privacy(ICSP), Korea Univ.
"""

class Sbox:
    def __init__(self, sbox=None):
        if type(sbox)==type(None):
            import warnings
            warnings.warn("S-box is not defined.", Warning)
        else:
            self.insert(sbox)
        pass

    ### If sbox is not defined
    # insert custom S-box 
    def insert(self, sbox):
        # check input is a 1-D table (or array).
        try:
            a = sbox[0]
            try:
                a = sbox[0][0] 
                # dim >= 2
                raise ValueError("It seems input is not a 1-D table.")
            except:
                self.sbox = sbox
        except: 
            # not table
            raise ValueError("It seems that S-box is not a box.")
        pass

