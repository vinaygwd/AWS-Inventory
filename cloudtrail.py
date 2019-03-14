# cloudTrail

import boto3
client = boto3.client('cloudtrail')
trail = client.describe_trails()
print('Name',"|",'S3BucketName',"|",'IncludeGlobalServiceEvents',"|",'IsMultiRegionTrail',"|","HomeRegion","|",'TrailARN')
for i in trail['trailList']:
    print(i['Name'],"|",i['S3BucketName'],"|",i['IncludeGlobalServiceEvents'],"|",i['IsMultiRegionTrail'],"|",i['HomeRegion'],"|",i['TrailARN'])
