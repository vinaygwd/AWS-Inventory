
# EIP

import boto3
client = boto3.client('ec2')
addresses_dict = client.describe_addresses()
for eip_dict in addresses_dict['Addresses']:
    print ("IP - ",eip_dict['PublicIp'] )
    if 'InstanceId' not in eip_dict:
        print("-------------------------------------")
        exit(0)
    if 'InstanceId' in eip_dict:
        print ("Instance_id - ", eip_dict['InstanceId'])
        print("-------------------------------------")
