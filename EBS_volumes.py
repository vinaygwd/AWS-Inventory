import boto3
client = boto3.client('ec2')
volume = client.describe_volumes()
print("Volume","   |   ","State","|","AZ","|","Size","|","Iops")
for i in volume['Volumes']:
    if i['Attachments'] is not None:
        print(i['VolumeId'],"|",i['State'],"|",i['AvailabilityZone'],"|",i['Size'],"|",i['Iops'])