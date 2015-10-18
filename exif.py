#!/usr/bin/env python

# Extract EXIF data from pictures --- namely, shutter speed, f-stop, and ISO.
# Requires ExifRead

import exifread

f = open("pics.txt", "r")

for line in f:
	img = open("DSC_{0}.JPG".format(line.strip()), "rb")

	tags = exifread.process_file(img)

	EXP = tags['EXIF ExposureTime']
	FNO = tags['EXIF FNumber']
	
	# try-except block in case ISO field is empty (Hi-1)

	try:
		ISO = " ISO {0}".format(tags['EXIF ISOSpeedRatings'])
	except KeyError:
		ISO = ""
	
	print "./DSC_{0}.JPG".format(line.strip())
	print ", {0} @ {1}{2}\n".format(EXP, FNO, ISO)
