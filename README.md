# Python_scripts_ECS

By using this Scripts we can automate the AWS ECS service.

# sample script to list tasks:

import boto3
import sys
client = boto3.client('ecs')
response = client.list_tasks(
    cluster=str(sys.argv[1]),
    desiredStatus='running'
)

print(response)

# usage

# while running the script pass cluster argument

python filename.py clustername
