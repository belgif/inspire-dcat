# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# gemet.py
# Created in: December   2019 by benoit fricheteau
# edited on: 
#
# Parameter: none
# 
# ---------------------------------------------------------------------------


import requests
import json
from jsonpath_rw_ext import parse



class conceptrdf(object):
    def __init__(self, session):
        self.session=session
           
    def _response (self,URL, params):
        self.URL=URL
        self.params=params
        self.concept=self.session.get(self.URL,params=self.params)       
    
    def findpreflabel(self, URI, language):
        self.language=language
        self.URI=URI
        data = { 
            'concept_uri':self.URI,
            'language':self.language
            }
        self._response('http://www.eionet.europa.eu/gemet/getConcept', data)
        self.json=self.concept.json()
        self.preflabel=self.json['preferredLabel']['string']
        
