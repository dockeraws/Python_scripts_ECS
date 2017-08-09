import boto3
import sys
client = boto3.client('ecs')
response = client.list_tasks(
    cluster=str(sys.argv[1]),
    desiredStatus='stopped'
)
tasks=response['taskArns']
taskArns="\n".join(tasks)
print(taskArns)

