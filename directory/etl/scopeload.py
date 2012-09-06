#!/usr/bin/env python
# encoding: utf-8
"""
etl_scope.py

Created by mikehas on 2012-08-28.
Copyright (c) 2012 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import re
import pickle
from pprint import pprint
import json

centers = []
cdir = '/Users/Shared/ScopeTheSitch/pphood/centers/'
data = '/Users/Shared/ScopeTheSitch/pphood/picklejar/'

def parsefiles(a, b, files):
  for file in files:
    f = open(os.path.join(cdir,file))
    text = f.read()
    if len(re.findall('Health center information is unavailable at this time', text)) == 0:
      c = {} 
      c['title'] = re.findall('class=\'center_home\'>(.*?)</a>', text)
      c['address'] = re.findall('class=\'street-address\'>(.*?)</span>', text)
      c['state'] = re.findall('class=\'center_state_abbr\'>(.*?)</span>', text)
      c['city'] = re.findall('class=\'center_city\'>(.*?)</span>', text)
      c['region'] = re.findall('class=\'region\'>(.*?)</span>', text)
      c['zipcode'] = re.findall('class=\'postal-code\'>(.*?)</span>', text)
      c['phone'] = re.findall('class=\'tel\'>([\-\.0-9]+)</span>', text)
  
      c['operatorlink'] = re.findall('Operated by\:.*?<a href=\'(.*?)\'>', text)
      c['operatorname'] = re.findall('Operated by\:.*?<a href=.*?>(.*?)</a>', text)
  
      c['googleaddress'] = re.findall('class=\'center_google_address\'>(.*?)</span>',text)
      c['days'] = ['Mon','Tues','Wed','Thurs','Fri','Sat','Sun']
      c['open'] = re.findall('<td>(.*?)</td>', ''.join(re.findall('<tr>.*?<td><strong>Open</strong></td>(.*?)</tr>',text)))
      c['close'] = re.findall('<td>(.*?)</td>', ''.join(re.findall('<tr>.*?<td><strong>Close</strong></td>(.*?)</tr>',text)))
      c['note'] = re.findall('<div class=\'note\'>(.*?)</div>', text)
      c['services'] = re.findall('\'>(.*?)<', "".join(re.findall('Services Offered.*?\'>(.*?)</ul>', text)) )

      centers.append(c)   

def doimport():
  pass

def loadcenters():
  pfile = os.path.join(data, "centers.p")
  pf = open(pfile, 'r')
  return pickle.load(pf)


class FixtureEngine:
  def __init__(self, appname):
    self.appname = appname
    self.fixtures = {}
    self.data = None

  def loaddata(self, data):
    self.data = data
      
  def createfixtures(self):
    locations = self.createlocations()
    self.fixtures['locations'] = locations
    # operators = self.createoperators()
    # self.fixtures['operators'] = operators
  
  def getfixtures(self):
    return self.fixtures
  
  def createlocations(self):
    pk = 0
    modelname = "Location"
    locations = []
    for i in self.data:
      c = {}
      c['model'] = self.appname + "." + modelname
      c['pk'] = pk
      c['fields'] = {
        "name": self.clean(i['title']),
        "note": self.clean(i['note']),
        "address": self.clean(i['address']),
        "city": self.clean(i['city']),
        "phone": self.clean(i['phone']),
        "zipcode": self.clean(i['zipcode']),
        "state": self.clean(i['state']),
        "region": self.clean(i['region']),
        "googleaddress": self.clean(i['googleaddress'])
      }
      locations.append(c)
      pk += 1
    return locations
    
    
  def clean(self,i):
    try:
      return i[0];
    except:
      return i
  
  
def main():
  actions = ['import', 'load', 'fixtures']
  if len(sys.argv) == 1:
    print "Incorrect Usage"
    sys.exit(1)
  action = sys.argv[1]
  if action not in actions:
    print "Unsupported Action"
    sys.exit(1)
  # os.path.walk(cdir, parsefiles, "None")
  if action == 'import':
    pass
  if action == 'load':
    print loadcenters()
  if action == 'fixtures':
    fix = FixtureEngine("directory")
    fix.loaddata(loadcenters())
    fix.createfixtures()
    print json.dumps(fix.getfixtures()['locations'], encoding="Windows-1252")
    
  # pf = open(pfile, 'w+')
  # pickle.dump(centers, pf)

  
if __name__ == '__main__':
  main()

