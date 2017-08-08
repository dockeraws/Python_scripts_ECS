
import boto3
import sys

client = boto3.client('ecs')

response = client.run_task(
    cluster=str(sys.argv[1]),
    taskDefinition=str(sys.argv[2])
)
print(response)
