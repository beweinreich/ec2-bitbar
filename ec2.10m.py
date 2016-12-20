#!/usr/bin/python

import boto3

client = boto3.client('ec2')
response = client.describe_instances()
reservations = response['Reservations']

ec2_instances = []

print "EC2"
print "---"

for reservation in reservations:
    for instance in reservation['Instances']:
        if 'Tags' in instance.keys():
            for tag in instance['Tags']:
                if tag['Key'] == "Name":
                    key_name = instance['KeyName']
                    ip = instance['PrivateIpAddress']
                    name = tag['Value']
                    ec2_instances.append({'name': name, 'ip': ip, 'key': key_name})


sorted = sorted(ec2_instances, key=lambda k: k['name'])
for item in sorted:
    bash_command = "ssh param1=-i param2=~/.ssh/%s.pem param3=ubuntu@%s" % (item['key'], item['ip'])
    print "%s | bash=%s" % (item['name'], bash_command)
    print item['ip']
    print "---"
