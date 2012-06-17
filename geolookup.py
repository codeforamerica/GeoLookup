#!/usr/bin/env python

import simplejson, urllib, sys, getopt

GEOCODE_BASE_URL = 'http://maps.googleapis.com/maps/api/geocode/json'

def geocode(address,sensor, **geo_args):
  geo_args.update({
    'address': address,
    'sensor': sensor
    })

  url = GEOCODE_BASE_URL + '?' + urllib.urlencode(geo_args)
  result = simplejson.load(urllib.urlopen(url))

  result = simplejson.dumps([s['geometry'] for s in result['results']])

  result = simplejson.loads(result)

  for item in result:
    print item['location']['lat']
    print item['location']['lng']

def make_addr(input):
  return input.replace(' ', '+')

def main(argv):
  addr = ''
  sens = 'false'
  try:
    opts, args = getopt.getopt(argv,"ha:s:",["address=","sensor="])
  except getopt.GetoptError:
    print 'geolookup.py -a <address> -s <sensor>'
    sys.exit(2)
  for opt, arg in opts:
    if opt == '-h':
      print 'geolookup.py -a <address> -s <sensor>'
      sys.exit()
    elif opt in ("-a", "--address"):
      addr = make_addr(arg)
    elif opt in ("-s", "--sensor"):
      sens = arg

    
  geocode(address=addr,sensor=sens)

if __name__ == '__main__':
  main(sys.argv[1:])
