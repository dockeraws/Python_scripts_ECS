import boto3
import sys
import json
client = boto3.client('ecs')
response = client.list_task_definitions(
    status='ACTIVE'
)

taskdef= response['taskDefinitionArns']
task_def="\n" .join(taskdef)

print task_def

