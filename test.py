#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  test.py
#  
#  Copyright 2017 BDS657 <laptop1@laptop1-Latitude-D830>
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
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


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
print j.cmlI
print j.cmlII
isinstance(d, float)		
print ("Decimal Day representing %s :  %f" % (d, d))
















