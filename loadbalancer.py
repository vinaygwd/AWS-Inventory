# Load Balancer details

import boto3
client = boto3.client('elbv2')
balancer = client.describe_load_balancers()

print("LoadBalancer Name",'|',"VPC",'|',"DNSName","|","Scheme")
for i in balancer['LoadBalancers']:
    print(i['LoadBalancerName'],'|',i['VpcId'],'|',i['DNSName'],'|',i['Scheme'])
