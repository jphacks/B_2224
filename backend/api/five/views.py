from django.shortcuts import render
from django.http import HttpResponse
import geojson
import json
import netCDF4

def api(request):
    infile="/Users/yuta/Downloads/B2022282_A1_WW00_chlora.nc"
    infile2="/Users/yuta/Downloads/B2022279_A1_WW00_chlora.nc"
    nc = netCDF4.Dataset(infile,'r')#'r'は読み込み指定
    nc2 = netCDF4.Dataset(infile2,'r')

    #grp = nc.groups['chlor_a']
    
    #var2 = grp.variables['変数名2'][:]
   
   
    data=nc.variables['chlor_a'].units#chlor_aはクロロフィル濃度
    
    return HttpResponse(data)

