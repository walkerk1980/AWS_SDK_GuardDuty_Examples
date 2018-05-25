#!/usr/bin/python
import boto3
import botocore
gd = boto3.client('guardduty')
s3 = boto3.client('s3')
detector=gd.list_detectors()
detectorid = detector['DetectorIds'][0]
sets = gd.list_threat_intel_sets(DetectorId=detectorid)
threatsetsetids = sets['ThreatIntelSetIds']
for threatsetsetid in threatsetsetids:
	setdesc = gd.get_threat_intel_set(DetectorId=detectorid, ThreatIntelSetId=threatsetsetid)
	print '\n' + 'Name: ' + setdesc['Name']
	print 'Status: ' + setdesc['Status']
	print 'Format: ' + setdesc['Format']
	print 'Location: ' + setdesc['Location'] + "\n"
	blLocation = setdesc['Location']
	blBucket = blLocation[blLocation.index("/",blLocation.index("/")+1)+1:blLocation.index("/",blLocation.index("/",blLocation.index("/")+1)+1)]
	blKey = blLocation[blLocation.index("/",blLocation.index("/",blLocation.index("/")+1)+1)+1:150]
	blContent = s3.get_object(Bucket=blBucket, Key=blKey)
	print 'ThreatIntelSet Content : \n\n' + blContent['Body'].read().decode('utf-8') + '\n\n'
