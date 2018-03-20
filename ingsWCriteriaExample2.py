#!/usr/bin/python
import boto3
gd = boto3.client('guardduty')
detector=gd.list_detectors()
detectorid = detector['DetectorIds'][0]
#Finding Critera for severity in this example must be greater than or equal to the value specified in Gte
fc={ 'Criterion': { 'severity': { 'Gte': 4}}}
findings = gd.list_findings(DetectorId=detectorid,FindingCriteria=fc)
for finding in findings['FindingIds']:
    finddetail = gd.get_findings(DetectorId=detectorid,FindingIds=[finding])
    print finddetail
    print "\n"
