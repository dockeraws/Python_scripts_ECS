import boto3
import sys
client = boto3.client('ecs')
response = client.list_tasks(
    cluster=str(sys.argv[1]),
   # containerInstance='2c3f3f0d-76db-42b2-8fdd-9edf1595e62e'
    desiredStatus='STOPPED'
)
print(response)
response = client.start_task(
    cluster=str(sys.argv[1]),
    taskDefinition='testapache',
    containerInstances=['2c3f3f0d-76db-42b2-8fdd-9edf1595e62e']

)
print(response)



