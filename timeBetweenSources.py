# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 13:57:38 2016

@author: Conor
"""

#!/usr/bin/env python

# To determine whether a particular source is above the horizon relative to the 
# Greenbank Radio Telescope.

# Enter our position first

# Enter the time at which we're viewing
#
# Location of source
#import warnings
import matplotlib.pyplot as plt

import numpy as np
from math import pi
from astropy import units as u
from astropy.time import Time
#import astropy.coordinates as coord
from astropy.coordinates import SkyCoord, EarthLocation, AltAz, Angle
#from astropy.utils import iers
#2016iers.IERS.iers_table = iers.IERS_A.open(iers.IERS_A_URL)
encoding = "utf-8"

GBT_ALT_SLEW = 17.6*(u.deg/u.min)
GBT_AZ_SLEW = 35.2*(u.deg/u.min)

#warnings.filterwarnings("ignore")
    
green_bank = EarthLocation(lat=38.433129*u.deg, lon=-79.83983858*u.deg, height=20*u.m)

#raw_input -> Python 2.x
#starting_time = raw_input("Enter start time for observation (YYYY-M-DD HH:MM:SS) UTC: ")
starting_time = input("Enter start time for observation (YYYY-M-DD HH:MM:SS) UTC: ")

time_start  = Time(starting_time, location=green_bank)
print(time_start.sidereal_time('mean'))

#raw_input -> Python 2.x
#ending_time = raw_input("Enter end time for observation (YYYY-M-DD HH:MM:SS) UTC: ")
ending_time = input("Enter end time for observation (YYYY-M-DD HH:MM:SS) UTC: ")

time_end = Time(ending_time, location=green_bank)
print(time_end.sidereal_time('mean'))

exo_RaDec = np.genfromtxt('unsorted.cat', dtype=None)

exo_AltAz = []

#Process array and convert every RA and DEC into altitude and azimuth for Greenbank for 16:00 UTC
for i in range(len(exo_RaDec)):
    
    source_Name = exo_RaDec[i][0].decode(encoding)
    source_RA = exo_RaDec[i][1].decode(encoding)
    source_DEC = exo_RaDec[i][2].decode(encoding)
    
    source_RA = source_RA[0:2] + 'h' + source_RA[3:5] + 'm' + source_RA[6:11] + 's'
    source_DEC = '+' + source_DEC[0:2] + 'd' + source_DEC[3:5] + 'm' + source_DEC[6:11] + 's'
    
    source = SkyCoord(source_RA, source_DEC)
    
    sourceAltAz_1 = source.transform_to(AltAz(obstime=time_start, location=green_bank))
    #sourceAltAz_2 = source.transform_to(AltAz(obstime=time_end, location=green_bank))
    
    exo_current = [source_Name, sourceAltAz_1.alt, sourceAltAz_1.az]
    exo_AltAz.append(exo_current)

#Now have the alt and az for every exoplanet a the the time relative to greenbacnk horizon. 

#Want to look at first planet and compute absolute difference between alt and az for first planet and every other planet.
exo_diff = []

for i in range(len(exo_AltAz)):
    #i corresponds to the current planet
    #Now need to loop through every other planet including itself(will be 0)
    altAz_diff = [] # All alt az differences for one planet
    for j in range(len(exo_AltAz)):
        diff_Alt = abs(exo_AltAz[i][1] - exo_AltAz[j][1])
        diff_Az = abs(exo_AltAz[i][2] - exo_AltAz[j][2])
        
        altAz_diff_current = np.amax([((diff_Alt.value)/(GBT_ALT_SLEW.value))*(60), ((diff_Az.value)/(GBT_AZ_SLEW.value))*(60)])#Alt az difference between planet i and j
        altAz_diff.append(altAz_diff_current)
    
    exo_diff.append(altAz_diff)
    
#Now with the table of max times between every exoplanet and every other exoplanet we can start 
#implementing a solution/approximate solution to the travelling salesman problem. 
    
#Generate permutation 

#########################
current_time = 1000
planets_chosen = []

for i in range(len(exo_diff)):
    #####NOT RIGHT#####
    min_time_current = exo_diff[i][0]
    for j in range(len(exo_diff)):
        if((exo_diff[i][j] != 0) and (exo_diff[i][j] < min_time_current) and (j not in (planets_chosen))):
            min_time_current = exo_diff[i][j]
            min_planet = j
    
    planets_chosen.append(min_planet)
########################