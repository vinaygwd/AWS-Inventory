# Lambda fuction query
 
import boto3
client = boto3.client('lambda')
test = client.list_functions()
print('FunctionName',"|",'Role')
for i in test['Functions']:
    print(i['FunctionName'],"|",i['Role'])
