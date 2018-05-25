#!/usr/bin/python
import boto3
import botocore
gd = boto3.client('guardduty')
s3 = boto3.client('s3')
detector=gd.list_detectors()
detectorid = detector['DetectorIds'][0]
sets = gd.list_ip_sets(DetectorId=detectorid)
ipsetids = sets['IpSetIds']
for ipsetid in ipsetids:
	setdesc = gd.get_ip_set(DetectorId=detectorid, IpSetId=ipsetid)
	print '\n' + 'Name: ' + setdesc['Name']
	print 'Status: ' + setdesc['Status']
	print 'Format: ' + setdesc['Format']
	print 'Location: ' + setdesc['Location'] + "\n"
	wlLocation = setdesc['Location']
	wlBucket = wlLocation[wlLocation.index("/",wlLocation.index("/")+1)+1:wlLocation.index("/",wlLocation.index("/",wlLocation.index("/")+1)+1)]
	wlKey = wlLocation[wlLocation.index("/",wlLocation.index("/",wlLocation.index("/")+1)+1)+1:150]
	wlContent = s3.get_object(Bucket=wlBucket, Key=wlKey)
	print 'WhiteList Content : \n\n' + wlContent['Body'].read().decode('utf-8') + '\n\n'
