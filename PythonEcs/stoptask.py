import boto3
import sys

client = boto3.client('ecs')

response = client.stop_task(
    cluster=str(sys.argv[1]),
    task=str(sys.argv[2])
)
print(response)
