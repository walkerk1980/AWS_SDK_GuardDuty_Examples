#!/usr/bin/python
import boto3
gd = boto3.client('guardduty')
detector=gd.list_detectors()
detectorid = detector['DetectorIds'][0]
#Finding Critera for type in this example can be equal to either of the two values specified in Eq
fc={ 'Criterion': { 'type': { 'Eq': ['Recon:EC2/PortProbeUnprotectedPort', 'Recon:EC2/Portscan']}}}
findings = gd.list_findings(DetectorId=detectorid,FindingCriteria=fc)
for finding in findings['FindingIds']:
    finddetail = gd.get_findings(DetectorId=detectorid,FindingIds=[finding])
    print finddetail
    print "\n"
