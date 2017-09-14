# -*- coding: utf-8 -*-
"""
Created on Fri Sep 01 14:50:41 2017

@author: Selina

"""

##---Import modules
import os
import sys
import netCDF4
import sched, time
import numpy as np
from netCDF4 import Dataset


##---Go to file directory in local drive
os.chdir('E:\\Selina\\National_Water_Model_Nodes')    
dataset0 = Dataset('nwm.t00z.analysis_assim.channel_rt.tm00.conus.nc')

##---Check data attributes
for attr in dataset0.ncattrs():
    print (attr, '=', getattr(dataset0, attr))
    
    
##---Check the data format
#print (dataset0.file_format)
#print (dataset0.dimensions.keys())
#print (dataset0.dimensions['time'])
#print (dataset0.variables.keys())
#print (dataset0.variables['streamflow'])
#print (dataset0.variables['q_lateral'])
#print (dataset0.Conventions)
#print (streamflow.units)

   
##---Get all available data
stream_flow = np.array(dataset0.variables['streamflow'])
reach_id = np.array(dataset0.variables['feature_id'])
lateral_flow = np.array(dataset0.variables['q_lateral'])


##---Get the data using url

#nc_fid = Dataset('http://nomads.ncep.noaa.gov/pub/data/nccf/com/nwm/prod/nwm.20170910/analysis_assim/nwm.t00z.analysis_assim.channel_rt.tm00.conus.nc')
#nc = Dataset(nc_fid, 'r')


url = 'http://nomads.ncep.noaa.gov/pub/data/nccf/com/nwm/prod/nwm.20170910/analysis_assim/nwm.t00z.analysis_assim.channel_rt.tm00.conus.nc'
dataset = netCDF4.Dataset(url)