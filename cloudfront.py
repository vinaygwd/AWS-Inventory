#cloudfront

import boto3
client = boto3.client('cloudfront')
cloudfront = client.list_distributions()
print('Id','|','Status','|','DomainName','|','Name','|','DomainName')
for i in cloudfront['DistributionList']['Items']:
    print(i['Id'],'|',i['Status'],'|',i['DomainName'],'|',i['Origins']['Items'][0]['Id'],'|',i['Origins']['Items'][0]['DomainName'])
