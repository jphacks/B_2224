# command に先に ncdump　-h 'path/file'　で中身をチェックするでも可
import netCDF4
import sys
import numpy as np
# ファイルを開く
infile="/Users/aorimbe/Downloads/B2022001_A1_WW00_chlora.nc"
nc = netCDF4.Dataset(infile,'r')
# ーーーーーーーーーーーーーーーーー

#次元の情報を入手する
print (nc.dimensions) 
lon = 4320
lat = 2160
rgb = 3
eightbitcolor = 256
time = 1
altitude = 1

#データを読み込む
data=nc.variables['chlor_a'][:]

for i in range(lon):
	for j in range(lat):
		dat=data[0,0,i,j]
		print(dat)#出力

