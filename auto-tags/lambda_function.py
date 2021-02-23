import boto3
import csv



ec2 = boto3.resource('ec2')

id_instance = 'i-08e0a2af10f0a0781'

def lambda_handler(event, context):

    ec2.create_tags(
        Resources=['i-08e0a2af10f0a0781'], 
        Tags=[  {"Key": "dasdasd","Value": "asdasda"},
                {"Key": "name","Value": "apphostname"},
                {"Key": "teste1","Value": "teste2"},
                {"Key": "testew","Value": "teasdasd"}
            ]
        )
        
    ec2.create_tags(
        Resources=['i-08e0a2af10f0a0781'], 
        Tags=[  {"Key": "dasdasd","Value": "asdasda"},
                {"Key": "name","Value": "apphostname"},
                {"Key": "teste1","Value": "teste2"},
                {"Key": "testew","Value": "teasdasd"}
            ]
        )
    
with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)