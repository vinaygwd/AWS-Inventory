import boto3
client = boto3.client('ec2')
volume = client.describe_volumes()
for i in volume['Volumes']:
    if i['Attachments'] != []:
        if 'InstanceId' in i['Attachments'][0]:
            print(i['Attachments'][0]['InstanceId'],"|",i['VolumeId'],"|",i['State'],"   |",i['Iops'],"|",i['Size'])
    else:
        print("                   ","|",i['VolumeId'],"|",i['State'],"|",i['Iops'],"|",i['Size'])
