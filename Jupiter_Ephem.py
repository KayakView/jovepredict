#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Jupiter_Ephem.py
#  
#  Copyright 2017 Rob Walker, Bothell WA
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.

import ephem

d = raw_input("Date?  yyyy/mm/dd: ")
lname = raw_input("Location name? ")
la = raw_input("Latitude?  dd.dddd: ")
lo = raw_input("Longitude? (-'ve West)  dd.dddd: ")

a = ephem.Observer()
a.date = d
a.lat = la
a.lon = lo

j = ephem.Jupiter()

print
print "Jupiter Data for %s" % (lname)
print "--------------------------"
print
print "Rise"
print(a.next_rising(j))
print
print "Transit"
print(a.next_transit(j))
print
print "Set"
print(a.next_setting(j))
print

















